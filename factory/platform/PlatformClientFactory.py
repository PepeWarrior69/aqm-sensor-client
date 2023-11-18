from abc import ABC, abstractmethod
from strategy.platform import PlatformClientStrategy, TestLinuxClientStrategy, TestWindowsClientStrategy, RaspberryClientStrategy, ArduineClientStrategy

class PlatformClientFactory(ABC):
    @abstractmethod
    def create_platform_client(self, url: str) -> PlatformClientStrategy:
        pass


class TestLinuxClientFactory(PlatformClientFactory):
    def create_platform_client(self, url: str) -> PlatformClientStrategy:
        return TestLinuxClientStrategy(url)

class TestWindowsClientFactory(PlatformClientFactory):
    def create_platform_client(self, url: str) -> PlatformClientStrategy:
        return TestWindowsClientStrategy(url)

class RaspberryClientFactory(PlatformClientFactory):
    def create_platform_client(self, url: str) -> PlatformClientStrategy:
        return RaspberryClientStrategy(url)

class ArduineClientFactory(PlatformClientFactory):
    def create_platform_client(self, url: str) -> PlatformClientStrategy:
        return ArduineClientStrategy(url)

