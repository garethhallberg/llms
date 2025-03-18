If you need to place the `api_key_checker.py` file in a folder, you can organize your project structure and adjust your import statements accordingly. Here's a step-by-step guide on how to do this:

### Step 1: Organize Your Project Structure

Let's assume you want to place the `api_key_checker.py` file in a folder named `utils`. Your project structure might look like this:

```
my_project/
│
├── main_script.py
│
└── utils/
    └── api_key_checker.py
```

### Step 2: Update the `api_key_checker.py` File

The `api_key_checker.py` file remains the same as before:

```python
# utils/api_key_checker.py

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

### Step 3: Update the Import Statement in `main_script.py`

To import the `APIKeyChecker` class from the `utils` folder, you need to use a relative import or modify your `PYTHONPATH`. Here's how you can do it with a relative import:

```python
# main_script.py

from utils.api_key_checker import APIKeyChecker

# Create an instance of APIKeyChecker
checker = APIKeyChecker()

# Retrieve the OpenAI API key
openai_api_key = checker.get_openai_api_key()

# You can then use the key as needed
if openai_api_key:
    print(f"Retrieved OpenAI API Key: {openai_api_key[:8]}...")
else:
    print("OpenAI API Key not available.")
```

### Step 4: Ensure the Folder is Recognized as a Package

For the `utils` folder to be recognized as a package, you need to include an `__init__.py` file within it. This file can be empty, but its presence tells Python that the directory should be treated as a package.

```
my_project/
│
├── main_script.py
│
└── utils/
    ├── __init__.py
    └── api_key_checker.py
```

### Step 5: Run Your Script

You can now run your `main_script.py` from the project root directory (`my_project/`). Make sure that your `.env` file is also located in the project root directory, or adjust the path in the `load_dotenv()` call if necessary.

If you encounter any issues with imports, make sure that you're running the script from the correct directory or adjust your `PYTHONPATH` environment variable to include the project root directory.

By following these steps, you should be able to successfully use the `APIKeyChecker` class from a file located in a separate folder within your project.