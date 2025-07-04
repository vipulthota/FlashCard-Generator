# PPTX Presentation Generator

A Flask web application that generates PowerPoint presentations and flashcards using AI technology (OpenAI GPT). The application also provides Excel file analysis and report generation capabilities.

## Features

- **PPT Generator**: Create educational presentations with AI-generated content
- **Flashcard Generator**: Generate flashcards from Google Cloud Storage content
- **Excel Analysis**: Upload and analyze Excel files with automated report generation
- **Modern Web Interface**: Clean, responsive web interface for all features

## Prerequisites

- Python 3.8+
- OpenAI API key
- Google Cloud Storage service account (for flashcard feature)
- Excel files for analysis feature

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PPTX-Presentation-Generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration files**

   ### OpenAI API Configuration
   Edit `config/config.json`:
   ```json
   {
       "api_key": "YOUR_OPENAI_API_KEY_HERE",
       "save_location": "./generated_presentations"
   }
   ```

   ### Google Cloud Service Account (Optional - for flashcard feature)
   Replace the content in `service-account-key.json` with your actual service account credentials:
   ```json
   {
       "type": "service_account",
       "project_id": "YOUR_PROJECT_ID",
       "private_key_id": "YOUR_PRIVATE_KEY_ID",
       "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n",
       "client_email": "YOUR_SERVICE_ACCOUNT_EMAIL",
       "client_id": "YOUR_CLIENT_ID",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
       "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/YOUR_SERVICE_ACCOUNT_EMAIL",
       "universe_domain": "googleapis.com"
   }
   ```

4. **Update app.py configuration**
   
   In `app.py`, update the following variables with your actual values:
   ```python
   # Google Cloud Storage setup (if using flashcard feature)
   BUCKET_NAME = "YOUR_BUCKET_NAME"
   FOLDER_PATH = "YOUR_FOLDER_PATH"
   ```

## Getting API Keys

### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into `config/config.json`

### Google Cloud Service Account (Optional)
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Cloud Storage API
4. Go to IAM & Admin → Service Accounts
5. Create a new service account
6. Download the JSON key file
7. Replace content in `service-account-key.json`

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Navigate through different features using the web interface

3. **Features Usage**
   - **PPT Generator**: Enter topic, subject, class, and number of slides
   - **Flashcard Generator**: Browse available content from Google Cloud Storage
   - **Excel Analysis**: Upload Excel files for automated analysis and reporting

## Project Structure

```
PPTX-Presentation-Generator/
├── app.py                 # Main Flask application
├── generate_ppt.py        # PPT generation logic
├── report_generator.py    # Excel analysis and reporting
├── requirements.txt       # Python dependencies
├── config/
│   └── config.json       # OpenAI API configuration
├── apis/
│   ├── base_generation_api.py
│   └── openai_api.py     # OpenAI API integration
├── templates/            # HTML templates
│   ├── index.html
│   ├── main.html
│   ├── flashcardgenerator.html
│   └── analysis.html
├── static/               # CSS, JS, images
├── images/              # Generated slide images
├── uploads/             # Uploaded Excel files
└── reports/             # Generated analysis reports
```

## Dependencies

- Flask 3.1.0 - Web framework
- OpenAI 1.60.2 - AI text generation
- python-pptx 0.6.21 - PowerPoint file creation
- requests 2.31.0 - HTTP requests
- google-cloud-storage - Google Cloud integration (if using flashcard feature)

## Troubleshooting

1. **API Key Issues**
   - Ensure your OpenAI API key is valid and has sufficient credits
   - Check that the API key is properly formatted in `config/config.json`

2. **Google Cloud Issues**
   - Verify service account has proper permissions
   - Check that the JSON file is properly formatted
   - Ensure Cloud Storage API is enabled

3. **File Upload Issues**
   - Check file permissions in upload directory
   - Ensure supported file formats are being used

## Security Notes

- Never commit API keys or service account files to version control
- Use environment variables for sensitive configuration in production
- Regularly rotate API keys and service accounts
- Implement proper authentication for production deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the documentation
3. Create an issue in the repository

---

**Note**: This application uses AI services that may incur costs. Monitor your API usage and set appropriate limits.
