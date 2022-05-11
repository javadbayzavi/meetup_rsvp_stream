from workers.worker import worker


class publisher(worker):
    def __init__(self, broker) -> None:
        self.broker = broker
    
    def processMe(self):
        #publishing starts from here
        self.pushResult()
        pass
    
    def pushResult(self):
        pass
    