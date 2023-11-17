from abc import ABC, abstractmethod
from typing import List
from model import Packet
from service import HttpService
from strategy.sensor import SensorStrategy

class PlatformClientStrategy(ABC):
    def __init__(self, url: str):
        self.sensors: List[SensorStrategy] = []
        self.http = HttpService(url)
        self.packet = Packet(self.mac, self.ip)
        
    @property
    @abstractmethod
    def mac() -> str:
        pass
    
    @property
    @abstractmethod
    def ip() -> str:
        pass
    
    def read(self) -> bool:
        has_failed_read = False
        
        for sensor in self.sensors:
            try:
                data = sensor.read_data()
                self.packet.add(sensor.id, sensor.type, data)
            except Exception as err:
                print(f"Failed to read data {err=}")
                print(f"Failed to read data for {sensor=}")
                has_failed_read = True
        
        return has_failed_read
    
    def send_packet(self):
        try:
            if self.http.post(self.packet.to_JSON()):
                self.packet = Packet(self.mac, self.ip)
                
                return True
        except Exception as err:
            print("Error occured during _send_packet err=", err)
            
            return False


    
