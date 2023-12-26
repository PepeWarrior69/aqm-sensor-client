from .abstraction import SensorStrategy
import time
import random
import math

class TestSensorStrategy(SensorStrategy):
    @property
    def type(self):
        return "test"
    
    def read_data(self):
        # Generate values using a sine function with time
        value = 500 + 300 * math.sin(time.time())

        # Add some randomness
        value += random.uniform(-50, 50)

        # Ensure values are in the range [0, 1000]
        value = max(0, min(1000, value))
        
        return {
            "ts": int(time.time()),
            "value": round(value, 2)
        }
    
    def cleanup(self):
        pass
