from strategy.sensor import MQ2GasSensorStrategy
from .abstraction import PlatformClientStrategy
import socket
import uuid

class RaspberryClientStrategy(PlatformClientStrategy):
    @property
    def mac(self):
        return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    
    @property
    def ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google's DNS server
        ip_address = s.getsockname()[0]
        s.close()
        
        return ip_address
        
    def add_connected_sensors(self):
        self.sensors.append(
            MQ2GasSensorStrategy()
        )
