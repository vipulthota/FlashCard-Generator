# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Configuration
```bash
python setup.py
```

### 3. Configure API Keys

**OpenAI API Key** (Required):
- Edit `config/config.json`
- Replace `YOUR_OPENAI_API_KEY_HERE` with your actual API key

**Google Cloud Service Account** (Optional - for flashcard feature):
- Edit `service-account-key.json`
- Replace with your actual service account JSON

### 4. Update App Configuration
Edit `app.py` and replace:
```python
BUCKET_NAME = "YOUR_BUCKET_NAME"
FOLDER_PATH = "YOUR_FOLDER_PATH"
```

### 5. Run the Application
```bash
python app.py
```

### 6. Access the Application
Open your browser and go to: `http://localhost:5000`

## 🎯 Features Overview

### PPT Generator
- Create educational presentations with AI
- Customize number of slides, topic, subject, and class level
- Download as PowerPoint file

### Flashcard Generator
- Browse content from Google Cloud Storage
- Generate flashcards from existing educational content
- Visual flashcard interface

### Excel Analysis
- Upload Excel files for analysis
- Automated report generation
- Download detailed analysis reports

## 🔧 Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your OpenAI API key is valid and has credits
2. **Google Cloud Error**: Check service account permissions and file format
3. **File Upload Error**: Ensure upload directory has write permissions

### Need Help?
- Check the main README.md for detailed documentation
- Review SECURITY.md for security best practices
- Check the troubleshooting section in README.md

---

🎉 **You're ready to go!** Start creating presentations and analyzing data with AI-powered tools.
