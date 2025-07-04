from google.cloud import storage

# 🔹 Path to your service account JSON key file
SERVICE_ACCOUNT_JSON = "service-account-key.json"

# 🔹 Google Cloud Storage details
BUCKET_NAME = "cdn-mcb.myclassboard.com"
FOLDER_PATH = "ict-teacher-training/PPTGenerator/"  # Folder inside GCS

def list_files_in_gcs():
    """Lists all files in a specific GCS folder."""
    client = storage.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)
    bucket = client.bucket(BUCKET_NAME)

    # 🔹 Get all files in the folder
    blobs = bucket.list_blobs(prefix=FOLDER_PATH)

    file_list = [blob.name for blob in blobs]
    
    if file_list:
        print("✅ Files in GCS folder:")
        for file in file_list:
            print(f"- {file}")
    else:
        print("❌ No files found in the folder.")

# 🔹 Fetch and print file list
list_files_in_gcs()
# gs://cdn-mcb.myclassboard.com/ict-teacher-training/PPTGenerator/V/English/Parts_of_Speech.json
# ✅ File uploaded to GCS: gs://cdn-mcb.myclassboard.com/ict-teacher-training/PPTGenerator/V/English/Parts_of_Speech.json
# 202.65.129.235 - - [17/Mar/2025 11:17:55] "POST /generate_content HTTP/1.1" 200 -
# ✅ File uploaded to GCS: gs://cdn-mcb.myclassboard.com/ict-teacher-training/PPTGenerator/IV/Math/NUmbers.json
# 202.65.129.235 - - [17/Mar/2025 11:21:18] "POST /generate_content HTTP/1.1" 200 -
