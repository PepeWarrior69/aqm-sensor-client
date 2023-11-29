from time import sleep
from fastapi import FastAPI
from pydantic import BaseModel
from threading import Thread
from app import App


class AppWrapper:
    def __init__(self):
        self.sensor_app = None
        self.thread = None
        self.state = "inactive"
    
    def app_thread_worker(self, endpoint_url: str, platform: str):
        self.sensor_app = App()
        self.sensor_app.main(endpoint_url, platform, False)
        self.state = "active"
        
        while self.state == "active":
            sleep(1)
        
    def start(self, endpoint_url: str, platform: str):
        self.thread = Thread(target=self.app_thread_worker, args=(endpoint_url, platform,))
        self.thread.start()
        
        while self.state == "inactive":
            sleep(0.01)
        
    def stop(self):
        if not self.sensor_app or self.state == "inactive" or not self.thread:
            return
        
        self.sensor_app.cleanup()
        self.state = "inactive"
        self.thread.join()
        self.thread = None
        self.sensor_app = None
    
app_wrapper = AppWrapper()

def get_app_wrapper() -> AppWrapper:
    return app_wrapper


server_app = FastAPI()

class InitPayload(BaseModel):
    endpoint_url: str
    platform: str

@server_app.post("/api/init")
def init(body: InitPayload):
    wrapper = get_app_wrapper()
    wrapper.stop()
    wrapper.start(body.endpoint_url, body.platform)
    
    return { "mac": wrapper.sensor_app.platform_context.strategy.mac if wrapper.sensor_app else None }


@server_app.post("/api/deinit")
def deinit():
    wrapper = get_app_wrapper()
    wrapper.stop()

    return "OK"


# cleanup sensor_app in case of server_app shutdown
def before_server_shutdown():
    wrapper = get_app_wrapper()
    wrapper.stop()

server_app.add_event_handler("shutdown", before_server_shutdown)
