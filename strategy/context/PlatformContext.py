from service import BackgroundScheduleService
from strategy.platform.abstraction import PlatformClientStrategy
from config import SENSOR_READ_FREYENCY_SEC, SEND_DATA_FREQUENCY_SEC

class PlatformContext:
    def __init__(self, strategy: PlatformClientStrategy):
        self.bg_service = BackgroundScheduleService()
        self.strategy = strategy
        print(f"test_linux client {strategy.mac=}")
        print(f"test_linux client {strategy.ip=}")
    
    def start(self):
        self.read_bg_service_id = self.setup_bg_service(self.strategy.read, SENSOR_READ_FREYENCY_SEC)
        self.http_bg_service_id = self.setup_bg_service(self.strategy.send_packet, SEND_DATA_FREQUENCY_SEC)
        print("read_bg_service_id = ", self.read_bg_service_id)
        print("http_bg_service_id = ", self.http_bg_service_id)
    
    
    def setup_bg_service(self, job, interval_sec):
        id = self.bg_service.add_background_job(job, interval_sec)
        self.bg_service.start(id)
        
        return id

