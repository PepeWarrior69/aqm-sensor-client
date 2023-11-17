from abc import ABC, abstractmethod
import uuid

class SensorStrategy(ABC):
    def __init__(self):
        self.id = str(uuid.uuid4())
    
    @property
    @abstractmethod
    def type(self):
        pass
    
    @abstractmethod
    def read_data() -> dict:
        pass
    
