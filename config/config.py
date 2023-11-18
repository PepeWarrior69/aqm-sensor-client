from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
endpoint_url = os.getenv("ENDPOINT_URL")
