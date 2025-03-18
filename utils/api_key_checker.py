# api_key_checker.py

import os
from dotenv import load_dotenv

class APIKeyChecker:
    def __init__(self):
        load_dotenv()  # Load the .env file
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.xai_api_key = os.getenv('XAI_API_KEY')

    def check_keys(self):
        if self.openai_api_key:
            print(f"OpenAI API Key exists and begins {self.openai_api_key[:8]}")
        else:
            print("OpenAI API Key not set")

        if self.xai_api_key:
            print(f"XAI API Key exists and begins {self.xai_api_key[:8]}")
        else:
            print("XAI API Key not set")

    def get_openai_api_key(self):
        return self.openai_api_key
    
    def get_xai_api_key(self):
        return self.xai_api_key