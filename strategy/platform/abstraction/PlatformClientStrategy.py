from abc import ABC, abstractmethod
from typing import List
from model import Packet
from service import HttpService
from strategy.sensor import SensorStrategy
from requests import get
import json
import socket

class PlatformClientStrategy(ABC):
    def __init__(self, url: str):
        self._internal_ip = None
        self._external_ip = None
        self.sensors: List[SensorStrategy] = []
        self.http = HttpService(url)
        self.packet = Packet(self.mac, self.external_ip)
        self.add_connected_sensors()
        
    @property
    @abstractmethod
    def mac() -> str:
        pass
    
    @property
    def external_ip(self) -> str:
        try:
            if not self._external_ip:
                self._external_ip = get('https://api.ipify.org').content.decode('utf8')
            
            return self._external_ip
        except Exception as e:
            print(f"Error getting External IP address: {e}")
            return None
    
    @property
    def internal_ip(self) -> str:
        if not self._internal_ip:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(('192.255.255.255', 1))
                ip = s.getsockname()[0]
            except:
                ip = None
            finally:
                s.close()
            self._internal_ip = ip
        
        return self._internal_ip
    
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
            # print("self.packet.packet_data = ", json.dumps(self.packet.packet_data, indent=2))
            data = json.dumps(self.packet.packet_data)
            self.packet = Packet(self.mac, self.external_ip)
            
            if self.http.post(data):
                return True
        except Exception as err:
            print("Error occured during send_packet err=", err)
            
            return False

    def cleanup(self):
        for sensor in self.sensors:
            sensor.cleanup()
    
    
