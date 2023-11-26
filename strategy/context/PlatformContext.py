from service import BackgroundScheduleService
from strategy.platform.abstraction import PlatformClientStrategy
from config import SENSOR_READ_FREQUENCY_SEC, SEND_DATA_FREQUENCY_SEC

class PlatformContext:
    def __init__(self, strategy: PlatformClientStrategy):
        self.bg_service = BackgroundScheduleService()
        self.strategy = strategy
        print(f"platform MAC={strategy.mac} IP={strategy.ip}")
        
    def __del__(self):
        self.strategy.cleanup()
        print("Destructor of PlatformContext finished cleanup")
    
    def start(self):
        if len(self.strategy.sensors) < 1:
            raise Exception("No sensors detected. exiting...")
        
        try:
            self.read_bg_service_id = self.setup_bg_service(self.strategy.read, SENSOR_READ_FREQUENCY_SEC)
            self.http_bg_service_id = self.setup_bg_service(self.strategy.send_packet, SEND_DATA_FREQUENCY_SEC)
            print("read_bg_service_id = ", self.read_bg_service_id)
            print("http_bg_service_id = ", self.http_bg_service_id)
        except Exception as err:
            print(f"Error during background service start {err=}")
            raise Exception(err)
    
    
    def setup_bg_service(self, job, interval_sec):
        id = self.bg_service.add_background_job(job, interval_sec)
        self.bg_service.start(id)
        
        return id

