from strategy.context.PlatformContext import PlatformContext
from strategy.platform import PlatformClientStrategy, TestLinuxClientStrategy, TestWindowsClientStrategy, RaspberryClientStrategy, ArduineClientStrategy
from config import ENDPOINT_URL
from typing import Dict
import argparse
import time

platform_strategy: Dict[str, PlatformClientStrategy] = {
    "test_linux": TestLinuxClientStrategy,
    "test_windows": TestWindowsClientStrategy,
    "raspberry_pi": RaspberryClientStrategy,
    "arduine": ArduineClientStrategy
}

class App:
    def main(self):
        self.parse_arguments()
        print("platform = ", self.args.platform)
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
        Strategy = platform_strategy.get(platform, None)
        
        if not Strategy:
            raise Exception(f"Strategy for platform {platform=} is not found")
        
        return Strategy(ENDPOINT_URL)

