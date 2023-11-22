from .abstraction import SensorStrategy
import time
import random

class TestSensorStrategy(SensorStrategy):
    @property
    def type(self):
        return "test"
    
    def read_data(self):
        return {
            "ts": int(time.time()),
            "value": random.randrange(400, 1000)
        }