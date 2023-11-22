from .abstraction import PlatformClientStrategy

class RaspberryClientStrategy(PlatformClientStrategy):
    @property
    def mac(self):
        pass
    
    @property
    def ip(self):
        pass
        
    def add_connected_sensors(self):
        pass
