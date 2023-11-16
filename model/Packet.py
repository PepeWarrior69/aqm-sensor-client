
class Packet:
    def __init__(self, mac):
        # make sure that bg workers won't set any values during cleanup 
        # if cleaning in process then worker should wait till it's finished and then set data
        is_cleaning = False
    
    def cleanup(self):
        self.is_cleaning = True
        # some reset logic to performm
        self.is_cleaning = True
    
    def to_JSON(self) -> dict:
        pass
    