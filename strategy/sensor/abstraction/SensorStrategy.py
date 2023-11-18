from abc import ABC, abstractmethod
import uuid

class SensorStrategy(ABC):
    def __init__(self):
        self.id = str(uuid.uuid4())[0:8]
    
    @property
    @abstractmethod
    def type(self):
        pass
    
    @abstractmethod
    def read_data(self) -> dict:
        pass
    
