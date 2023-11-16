from abc import ABC, abstractmethod

class SensorStrategy(ABC):
    @abstractmethod
    def test_sensor():
        pass
