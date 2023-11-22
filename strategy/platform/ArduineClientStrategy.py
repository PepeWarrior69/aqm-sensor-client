from .abstraction import PlatformClientStrategy

class ArduineClientStrategy(PlatformClientStrategy):
    @property
    def mac(self):
        pass
    
    @property
    def ip(self):
        pass
        
    def add_connected_sensors(self):
        pass
