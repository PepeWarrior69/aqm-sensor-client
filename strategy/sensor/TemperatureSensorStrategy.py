from .abstraction import SensorStrategy

class TemperatureSensorStrategy(SensorStrategy):
    @property
    def type(self):
        return "temperature"
    
    def read_data(self) -> dict:
        pass

    def cleanup(self):
        pass
