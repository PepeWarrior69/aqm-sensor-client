from dataclasses import dataclass, asdict
from typing import List, Dict, Union

@dataclass
class PacketData:
    mac: str
    ip: str
    body: Dict[
        str, Dict[
            str, Union[str, List[dict]]
        ]
    ]
    

class Packet:
    def __init__(self, mac, ip):
        # make sure that bg workers won't set any values during cleanup 
        # if cleaning in process then worker should wait till it's finished and then set data
        self.is_cleaning = False
        # self._packet_data = {
        #     "mac": mac,
        #     "ip": ip,
        #     "body": {}
        # }
        self._packet_data = PacketData(mac, ip, {})
    
    def cleanup(self):
        self.is_cleaning = True
        # some reset logic to performm
        self.is_cleaning = True
        
    def add(self, sensor_id: str, type: str, sensor_data: dict):
        body = self._packet_data.body
        
        if sensor_id not in body:
            body[sensor_id] = {
                "type": type,
                "data": []
            }
        
        body[sensor_id]["data"].append(sensor_data)
    
    def to_JSON(self) -> dict:
        pass
    
    @property
    def packet_data(self):
        return asdict(self._packet_data)

