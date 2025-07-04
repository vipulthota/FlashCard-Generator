# Security Policy

## Sensitive Information

This project has been cleaned of sensitive information for public sharing. The following files contain placeholder values that need to be replaced with your actual credentials:

### 🔒 Files to Configure

1. **`config/config.json`** - Contains OpenAI API key placeholder
2. **`service-account-key.json`** - Contains Google Cloud service account placeholder
3. **`app.py`** - Contains Google Cloud Storage configuration placeholders

### 🚨 Important Security Notes

- **Never commit real API keys or service account files to version control**
- **Use environment variables for sensitive configuration in production**
- **Regularly rotate API keys and service accounts**
- **Monitor API usage and set appropriate limits**

### 🛡️ Before Using This Application

1. Replace `YOUR_OPENAI_API_KEY_HERE` in `config/config.json` with your actual OpenAI API key
2. Replace the entire content of `service-account-key.json` with your actual Google Cloud service account JSON
3. Update the Google Cloud Storage configuration in `app.py`:
   - `BUCKET_NAME = "YOUR_BUCKET_NAME"`
   - `FOLDER_PATH = "YOUR_FOLDER_PATH"`

### 🔐 Production Security Recommendations

1. **Use Environment Variables**: Store sensitive data in environment variables instead of config files
2. **Implement Authentication**: Add user authentication for production deployment
3. **Use HTTPS**: Always use HTTPS in production
4. **Rate Limiting**: Implement rate limiting to prevent API abuse
5. **Input Validation**: Validate all user inputs thoroughly
6. **File Upload Security**: Implement proper file validation and sandboxing

### 📋 Security Checklist

- [ ] API keys are stored securely (not in code)
- [ ] Service account has minimal required permissions
- [ ] File uploads are validated and sandboxed
- [ ] Application is deployed with HTTPS
- [ ] Regular security updates are applied
- [ ] API usage is monitored and limited
- [ ] Authentication is implemented for production use

### 🚨 If You Find a Security Issue

If you discover a security vulnerability, please report it by creating an issue in the repository with the label "security". Do not include sensitive information in the issue description.

---

**Remember**: This application uses external APIs that may incur costs. Always monitor your usage and set appropriate limits.
