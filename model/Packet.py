from dataclasses import dataclass, asdict
from typing import List, Dict, Union
import uuid

@dataclass
class PacketData:
    id: str
    mac: str
    ip: str
    body: Dict[
        str, Dict[
            str, Union[str, List[dict]]
        ]
    ]
    

class Packet:
    def __init__(self, mac, ip):
        self._packet_data = PacketData(str(uuid.uuid4()), mac, ip, {})
        
    def add(self, sensor_id: str, type: str, sensor_data: dict):
        body = self._packet_data.body
        
        if sensor_id not in body:
            body[sensor_id] = {
                "type": type,
                "data": []
            }
        
        body[sensor_id]["data"].append(sensor_data)
        print(f"Added data to packet {sensor_id=} {type=} {sensor_data=}")
    
    def to_JSON(self) -> dict:
        pass
    
    @property
    def packet_data(self):
        return asdict(self._packet_data)

