import os
from dotenv import load_dotenv

load_dotenv()

def get_auth_headers():
    api_key = os.getenv("API_KEY")
    if api_key:
        return {"Authorization": f"Bearer {api_key}"}
    return {}
