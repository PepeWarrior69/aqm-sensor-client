# Unable to install this lib on windows or linux
# It's designed only for Raspberry Pi
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("!!! Unable to import RPi.GPIO !!!")

from .abstraction import SensorStrategy
import time

OUTPUT_PIN = 14

class MQ2GasSensorStrategy(SensorStrategy):
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(OUTPUT_PIN, GPIO.IN)
    
    @property
    def type(self):
        return "gas"
    
    def read_data(self) -> dict:        
        return {
            "ts": int(time.time()),
            "value": GPIO.input(OUTPUT_PIN) # GPIO.LOW = 0; GPIO.HIGH = 1 
        }
    
    def cleanup(self):
        GPIO.cleanup()
