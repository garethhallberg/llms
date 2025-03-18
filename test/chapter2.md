To encapsulate your code within a class that can be imported and used in other parts of your project, you can create a Python module. Here's how you can structure your code to achieve this:

First, create a file named `api_key_checker.py` (or any name you prefer) and define a class inside it. Here's an example of how you can do this:

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
```

To use this class in another Python script, you can import it and call its methods like so:

```python
# main_script.py

from api_key_checker import APIKeyChecker

# Create an instance of APIKeyChecker
checker = APIKeyChecker()

# Call the check_keys method to print the API key status
checker.check_keys()
```

Make sure that the `api_key_checker.py` file is in the same directory as your main script or in a directory that's included in your Python path.

Also, ensure that you have the `python-dotenv` package installed in your environment to use the `load_dotenv` function. You can install it using pip:

```bash
pip install python-dotenv
```

And remember to have a `.env` file in the root directory of your project with the following format to store your API keys:

```
OPENAI_API_KEY=your_openai_api_key_here
XAI_API_KEY=your_xai_api_key_here
```

This way, your API keys will be loaded from the `.env` file, and you can check their status using the `APIKeyChecker` class.