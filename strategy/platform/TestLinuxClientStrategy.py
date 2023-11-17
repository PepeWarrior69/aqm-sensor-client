from strategy.platform import PlatformClientStrategy
import socket
import uuid

class TestLinuxClientStrategy(PlatformClientStrategy):    
    @property
    def mac(self):
        try:
            return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        except Exception as e:
            print(f"Error getting MAC address: {e}")
            return None
    
    @property
    def ip(self):
        try:
            host_name = socket.gethostname()
            ip_address = socket.gethostbyname(host_name)
            
            return ip_address
        except socket.error as e:
            print(f"Error getting IP address: {e}")
            return None
    
    