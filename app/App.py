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
    def main(self):
        self.parse_arguments()
        self.platform_context = PlatformContext(
            self.get_strategy_from_platform(self.args.platform)
        )
        
        self.platform_context.start()
        
        # prevent application exit
        while True:
            time.sleep(1)


    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Example script with named arguments')
        parser.add_argument('--platform', type=str, help='Specify the platform (e.g., raspberry, pc, arduino, test_linux, test_windows)')
        self.args = parser.parse_args()
        
    def get_strategy_from_platform(self, platform: str):
        if platform in platform_factory:
            print(f"Creating client for {platform=}")
            return platform_factory[platform].create_platform_client(ENDPOINT_URL)
        
        raise Exception(f"Strategy for platform {platform=} is not supported")
        

