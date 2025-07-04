#!/usr/bin/env python3
"""
Setup script for PPTX Presentation Generator
This script helps you configure the application by creating the necessary configuration files.
"""

import os
import json
import shutil

def create_config_files():
    """Create configuration files from templates"""
    
    # Create config.json from template
    config_template = "config/config.json.template"
    config_file = "config/config.json"
    
    if os.path.exists(config_template) and not os.path.exists(config_file):
        shutil.copy(config_template, config_file)
        print(f"✅ Created {config_file} from template")
        print("❗ Please edit config/config.json and add your OpenAI API key")
    elif os.path.exists(config_file):
        print(f"⚠️  {config_file} already exists")
    else:
        print(f"❌ Template {config_template} not found")
    
    # Create service-account-key.json from template
    service_template = "service-account-key.json.template"
    service_file = "service-account-key.json"
    
    if os.path.exists(service_template) and not os.path.exists(service_file):
        shutil.copy(service_template, service_file)
        print(f"✅ Created {service_file} from template")
        print("❗ Please edit service-account-key.json and add your Google Cloud service account credentials")
    elif os.path.exists(service_file):
        print(f"⚠️  {service_file} already exists")
    else:
        print(f"❌ Template {service_template} not found")

def create_directories():
    """Create necessary directories"""
    directories = [
        "images",
        "uploads", 
        "reports",
        "generated_presentations"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")
        else:
            print(f"⚠️  Directory already exists: {directory}")

def check_requirements():
    """Check if requirements.txt exists"""
    if os.path.exists("requirements.txt"):
        print("✅ requirements.txt found")
        print("💡 Run: pip install -r requirements.txt")
    else:
        print("❌ requirements.txt not found")

def main():
    print("🚀 Setting up PPTX Presentation Generator...")
    print("=" * 50)
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    # Create config files
    print("\n⚙️  Creating configuration files...")
    create_config_files()
    
    # Check requirements
    print("\n📦 Checking requirements...")
    check_requirements()
    
    print("\n" + "=" * 50)
    print("🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Edit config/config.json with your OpenAI API key")
    print("3. Edit service-account-key.json with your Google Cloud credentials (if using flashcard feature)")
    print("4. Run the application: python app.py")
    print("\n📖 For detailed instructions, see README.md")

if __name__ == "__main__":
    main()
