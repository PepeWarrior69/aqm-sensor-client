from abc import ABC, abstractmethod
from strategy import SensorStrategy
from strategy.sensor import Co2SensorStrategy, TemperatureSensorStrategy, TestSensorStrategy

class SensorFactory(ABC):
    @abstractmethod
    def create_sensor_strategy(self) -> SensorStrategy:
        pass

class Co2SensorFactory(SensorFactory):
    def create_sensor_strategy(self) -> SensorStrategy:
        return Co2SensorStrategy()

class TemperatureSensorFactory(SensorFactory):
    def create_sensor_strategy(self) -> SensorStrategy:
        return TemperatureSensorStrategy()

class TestSensorFactory(SensorFactory):
    def create_sensor_strategy(self) -> SensorStrategy:
        return TestSensorStrategy()

