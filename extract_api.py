import sys
import os
from library.get_api import get_api_key



if __name__ == "__main__":
    api_key = get_api_key()
    
    if api_key:
        print(f"API Key: {api_key}")
    else:
        print("No API key found.")

#add new key to DB and see if it reflects in UI