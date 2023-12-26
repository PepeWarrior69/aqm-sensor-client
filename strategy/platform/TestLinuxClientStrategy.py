from strategy.platform import PlatformClientStrategy
from strategy.sensor import TestSensorStrategy

class TestLinuxClientStrategy(PlatformClientStrategy):    
    @property
    def mac(self):
        try:
            # Get the MAC address on Linux reading eth0 interface
            with open(f'/sys/class/net/eth0/address') as file:
                mac_address = file.read().strip()
            return mac_address
        except Exception as e:
            print(f"Error getting MAC address on Linux: {e}")
            return None
        
    def add_connected_sensors(self):
        for _ in range(5):
            self.sensors.append(
                TestSensorStrategy()
            )
    
    