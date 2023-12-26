from strategy.platform import PlatformClientStrategy
import uuid

from strategy.sensor import TestSensorStrategy

class TestWindowsClientStrategy(PlatformClientStrategy):    
    @property
    def mac(self):
        try:
            return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        except Exception as e:
            print(f"Error getting MAC address on Windows: {e}")
            return None
        
    def add_connected_sensors(self):
        for _ in range(5):
            self.sensors.append(
                TestSensorStrategy()
            )
    
    