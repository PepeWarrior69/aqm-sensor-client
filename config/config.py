from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SENSOR_READ_FREQUENCY_SEC = int(os.getenv("SENSOR_READ_FREQUENCY_SEC")) if os.getenv("SENSOR_READ_FREQUENCY_SEC") else 5
SEND_DATA_FREQUENCY_SEC = int(os.getenv("SEND_DATA_FREQUENCY_SEC")) if os.getenv("SEND_DATA_FREQUENCY_SEC") else 30
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
PLATFORM = os.getenv("PLATFORM")

MQTT = {
    'HOST': os.getenv("MQTT_HOST"),
    'PORT': int(os.getenv("MQTT_PORT")),
    'KEEPALIVE': int(os.getenv("MQTT_KEEPALIVE"))
}

