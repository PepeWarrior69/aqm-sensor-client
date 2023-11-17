import requests

class HttpService:
    def __init__(self, url: str):
        self.url = url
        
    def post(self, packet: dict):
        try:
            res = requests.post(self.url, json=packet)
        
            if res.status_code < 300:
                print(f"Transfered packet to {self.url=} {packet=} res=", res)
                
                return True
            else:
                raise Exception(res)
        except Exception as err:
            print(f"Error in http request res=", err)
        
        return False

