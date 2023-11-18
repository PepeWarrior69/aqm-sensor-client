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
        self.add_connected_sensors()
        
    @property
    @abstractmethod
    def mac() -> str:
        pass
    
    @property
    @abstractmethod
    def ip() -> str:
        pass
    
    @abstractmethod
    def add_connected_sensors(self):
        pass

    
    def read(self) -> bool:
        print(f"Attempt to read data from sensors{{{ len(self.sensors) }}}")
        has_failed_read = False
        
        for sensor in self.sensors:
            try:
                data = sensor.read_data()
                self.packet.add(sensor.id, sensor.type, data)
            except Exception as err:
                print(f"Failed to read data {err=}")
                print(f"Failed to read data for {sensor.id=} {sensor.type=}")
                has_failed_read = True
        
        return has_failed_read
    
    def send_packet(self):
        try:
            packet = self.packet.packet_data
            self.packet = Packet(self.mac, self.ip)
            
            if self.http.post(packet):
                
                return True
        except Exception as err:
            print("Error occured during _send_packet err=", err)
            
            return False


    
