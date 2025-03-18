To add the functionality to retrieve the OpenAI API key, you can modify the `APIKeyChecker` class to include a method that returns the `openai_api_key`. Here's how you can update your `api_key_checker.py` file:

```python
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
```

With this addition, you can now call `get_openai_api_key()` on an instance of `APIKeyChecker` to retrieve the OpenAI API key. Here's how you can use it in another script:

```python
# main_script.py

from api_key_checker import APIKeyChecker

# Create an instance of APIKeyChecker
checker = APIKeyChecker()

# Retrieve the OpenAI API key
openai_key = checker.get_openai_api_key()

# You can then use the key as needed
if openai_key:
    print(f"Retrieved OpenAI API Key: {openai_key[:8]}...")
else:
    print("OpenAI API Key not available.")
```

This setup allows you to both check the status of your API keys and retrieve the OpenAI API key for use in other parts of your application.