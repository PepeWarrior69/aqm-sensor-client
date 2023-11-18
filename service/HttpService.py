import gzip
import requests

class HttpService:
    def __init__(self, url: str):
        self.url = url
        
    def post(self, payload: str):
        # print(f"Attempt to send packet to {self.url=} packet=", json.dumps(packet, indent=2))
        try:
            compressed_data = gzip.compress(payload.encode('utf-8'))
            headers = {'Content-Encoding': 'gzip', 'Content-Type': 'application/json'}
            
            print("payload str size = ", len(payload.encode('utf-8')))
            print("compressed_data size = ", len(compressed_data))
            
            res = requests.post(self.url, data=compressed_data, headers=headers)
        
            if res.status_code < 300:
                print(f"Transfered packet to {self.url=} res=", res)
                
                return True
            else:
                raise Exception(res)
        except Exception as err:
            print(f"Error in http request res=", err)
        
        return False

