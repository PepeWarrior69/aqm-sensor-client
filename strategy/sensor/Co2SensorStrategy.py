from .abstraction import SensorStrategy

class Co2SensorStrategy(SensorStrategy):
    @property
    def type(self):
        return "CO2"
    
    def read_data(self) -> dict:
        pass
