from service import BackgroundScheduleService
from strategy.platform.abstraction import PlatformClientStrategy

class PlatformContext:
    def __init__(self, strategy: PlatformClientStrategy):
        self.bg_service = BackgroundScheduleService()
        self.strategy = strategy
        print(f"test_linux client {strategy.mac=}")
        print(f"test_linux client {strategy.ip=}")
    
    def start(self):
        self.read_bg_service_id = self.setup_bg_service(self.strategy.read, 1)
        self.http_bg_service_id = self.setup_bg_service(self.strategy.send_packet, 10)
    
    
    def setup_bg_service(self, job, interval_sec):
        id = self.bg_service.add_background_job(job, interval_sec)
        self.bg_service.start(id)
        
        return id

