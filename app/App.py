from factory.platform import PlatformClientFactory, TestLinuxClientFactory, TestWindowsClientFactory, RaspberryClientFactory, ArduineClientFactory
from strategy.context.PlatformContext import PlatformContext
from config import ENDPOINT_URL
from typing import Dict
import argparse
import time

platform_factory: Dict[str, PlatformClientFactory] = {
    "test_linux": TestLinuxClientFactory(),
    "test_windows": TestWindowsClientFactory(),
    "raspberry_pi": RaspberryClientFactory(),
    "arduine": ArduineClientFactory()
}

class App:
    def __init__(self) -> None:
        self.platform_context = None
    
    def main(self, endpoint_url=ENDPOINT_URL, platform=None, prevent_exit=True):
        self.endpoint_url = endpoint_url
        
        if not platform: 
            self.parse_arguments()
            platform = self.args.platform
        
        self.platform_context = PlatformContext(
            self.get_strategy_from_platform(platform)
        )
        
        self.platform_context.start()
        
        if prevent_exit:
            while True:
                time.sleep(1)

    def cleanup(self):
        self.platform_context.cleanup()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Example script with named arguments')
        parser.add_argument('--platform', type=str, help='Specify the platform (e.g., raspberry_pi, arduine, test_linux, test_windows)')
        self.args = parser.parse_args()
        
    def get_strategy_from_platform(self, platform: str):
        if platform in platform_factory:
            print(f"Creating client for {platform=}")
            return platform_factory[platform].create_platform_client(self.endpoint_url)
        
        raise Exception(f"Strategy for platform {platform=} is not supported")
        

