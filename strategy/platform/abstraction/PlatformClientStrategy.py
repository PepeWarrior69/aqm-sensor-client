from abc import ABC, abstractmethod
from typing import List
from model import Packet
from service import HttpService
from strategy.sensor import SensorStrategy

class PlatformClientStrategy(ABC):
    def __init__(self):
        self.sensors: List[SensorStrategy] = []
        self.packet = Packet() # pass mac and any other required platform info
        self.http = HttpService() # pass url and port
    
    @abstractmethod
    def read(self):
        pass
    
    def _send_packet(self):
        try:
            self.http.post(self.packet.to_JSON())
            self.packet.cleanup()
        except Exception as err:
            print("Error occured during _send_packet err=", err)
    
