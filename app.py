from flask import Flask, render_template, request, jsonify, send_file
from generate_ppt import generate_ppt_content, generate_final_ppt
from report_generator import analyze_and_generate_report, get_analysis_summary, get_report_path
from google.cloud import storage
import os
import io
import json
import base64

app = Flask(__name__)

# Configuration - Replace with your actual values
IMAGES_FOLDER = "images"
UPLOAD_FOLDER = "uploads"

# Create directories if they don't exist
os.makedirs(IMAGES_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Google Cloud Storage setup
# TODO: Replace with your actual service account JSON file path
SERVICE_ACCOUNT_JSON = "service-account-key.json"
# TODO: Replace with your actual bucket name
BUCKET_NAME = "YOUR_BUCKET_NAME"
# TODO: Replace with your actual folder path
FOLDER_PATH = "YOUR_FOLDER_PATH"

# Initialize the Google Cloud Storage client
storage_client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)
bucket = storage_client.bucket(BUCKET_NAME)

@app.route('/')
def index():
    return render_template('main.html')

# ================= Flash Card Generator ROUTES =================
@app.route('/flashcardgenerator')
def flashcardgenerator():
    return render_template('flashcardgenerator.html')

@app.route('/get_classes')
def get_classes():
    try:
        blobs = storage_client.list_blobs(BUCKET_NAME, prefix=FOLDER_PATH + "/")
        classes = set()
        for blob in blobs:
            parts = blob.name.split('/')
            if len(parts) > 3:
                classes.add(parts[2])
        return jsonify({"classes": list(classes)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_subjects/<class_name>')
def get_subjects(class_name):
    try:
        prefix = f"{FOLDER_PATH}/{class_name}/"
        blobs = storage_client.list_blobs(BUCKET_NAME, prefix=prefix)
        subjects = set()
        for blob in blobs:
            parts = blob.name.split('/')
            if len(parts) > 4:
                subjects.add(parts[3])
        return jsonify({"subjects": list(subjects)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_topics/<class_name>/<subject>')
def get_topics(class_name, subject):
    try:
        prefix = f"{FOLDER_PATH}/{class_name}/{subject}/"
        blobs = storage_client.list_blobs(BUCKET_NAME, prefix=prefix)
        topics = [blob.name.split('/')[-1] for blob in blobs if blob.name.endswith('.json')]
        return jsonify({"topics": topics})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/save_image', methods=['POST'])
def save_image():
    try:
        data = request.json
        image_data = data['imageData']
        filename = data['filename']
        image_path = os.path.join(IMAGES_FOLDER, filename)

        # Decode the base64 image data
        image_data = image_data.split(",")[1]
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(image_data))

        return jsonify({"message": "Image saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ================= PPT GENERATOR ROUTES =================
@app.route('/pptgenerator')
def pptgenerator():
    return render_template('index.html')

@app.route('/generate_content', methods=['POST'])
def generate_content():
    try:
        topic = request.form.get('topic', '').strip()
        subject = request.form.get('subject', '').strip()
        class_name = request.form.get('class_name', '').strip()
        num_slides = request.form.get('num_slides', '0').strip()

        if not topic or not subject or not class_name or not num_slides:
            return jsonify({"error": "Missing required fields"}), 400

        num_slides = int(num_slides)
        slides = generate_ppt_content(topic, subject, class_name, num_slides)

        return jsonify({"slides": slides})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate', methods=['POST'])
def generate():
    try:
        topic = request.form.get('topic', '').strip()
        subject = request.form.get('subject', '').strip()
        class_name = request.form.get('class_name', '').strip()
        num_slides = request.form.get('num_slides', '0').strip()

        if not topic or not subject or not class_name or not num_slides:
            return jsonify({"error": "Missing required fields"}), 400

        num_slides = int(num_slides)

        slides = []
        for i in range(num_slides):
            title = request.form.get(f"slide_title_{i}", "").strip()
            content = request.form.get(f"slide_content_{i}", "").strip()
            slides.append({"title": title, "content": content})

        ppt = generate_final_ppt(topic, subject, class_name, slides)

        ppt_io = io.BytesIO()
        ppt.save(ppt_io)
        ppt_io.seek(0)

        return send_file(ppt_io, download_name=f'{topic}_presentation.pptx', as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/preview', methods=['POST'])
def preview():
    try:
        class_name = request.form.get('class_name', '').strip()
        subject = request.form.get('subject', '').strip()
        topic = request.form.get('topic', '').strip()

        if not class_name or not subject or not topic:
            return jsonify({"error": "Missing required fields"}), 400

        topic_path = f"{FOLDER_PATH}/{class_name}/{subject}/{topic}"
        blob = bucket.blob(topic_path)
        if not blob.exists():
            return jsonify({"error": "Topic file not found"}), 404

        content = json.loads(blob.download_as_text())

        return jsonify({"slides": content}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ================= ANALYSIS ROUTES =================
@app.route("/analysis")
def analysis():
    return render_template("analysis.html")  # Create a template for analysis upload page

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if not file.filename.endswith(('.xls', '.xlsx')):
        return jsonify({"error": "The uploaded file is not an Excel file."})

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    report_path, summary = analyze_and_generate_report(filepath)
    if "Error" in report_path:
        return jsonify({"error": report_path})

    return jsonify({"message": "File uploaded successfully"})

@app.route("/analysis_results")
def analysis_results():
    summary = get_analysis_summary()
    return jsonify(summary)

@app.route("/download_report")
def download_report():
    report_path = get_report_path()
    return send_file(report_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
