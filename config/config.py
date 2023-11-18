from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SENSOR_READ_FREYENCY_SEC = int(os.getenv("SENSOR_READ_FREQUENCY_SEC")) if os.getenv("SENSOR_READ_FREYENCY_SEC") else 1
SEND_DATA_FREQUENCY_SEC = int(os.getenv("SEND_DATA_FREQUENCY_SEC")) if os.getenv("SEND_DATA_FREQUENCY_SEC") else 10
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
