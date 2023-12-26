from strategy.sensor import MQ2GasSensorStrategy
from .abstraction import PlatformClientStrategy
import uuid

class RaspberryClientStrategy(PlatformClientStrategy):
    @property
    def mac(self):
        return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        
    def add_connected_sensors(self):
        self.sensors.append(
            MQ2GasSensorStrategy()
        )
