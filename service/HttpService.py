import requests

class HttpService:
    def __init__(self, url, port):
        self.url = url
        self.port = port
        
    def post(self, packet: dict):
        try:
            res = requests.post(self.url, json=packet)
        
            if res.status_code < 300:
                print(f"Transfered packet to {self.url=} {self.port=} {packet=} res=", res)
            else:
                raise Exception(res)
        except Exception as err:
            print(f"Error in http request res=", err)
            
    
