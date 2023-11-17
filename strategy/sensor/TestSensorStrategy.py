from .abstraction import SensorStrategy
import time
import random

class TestSensorStrategy(SensorStrategy):
    @property
    def type(self):
        return "test_sensor"
    
    def read_data() -> dict:
        return {
            "ts": time.time(),
            "value": random.randrange(400, 1000)
        }