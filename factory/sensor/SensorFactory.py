from abc import ABC, abstractmethod
from strategy import SensorStrategy

class SensorFactory(ABC):
    @abstractmethod
    def create_platform_client(self, url: str) -> SensorStrategy:
        pass
