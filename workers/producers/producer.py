from workers.worker import worker


class producer(worker):
    def __init__(self, broker) -> None:
        self.broker = broker
    
    def processMe(self):
        #production starts from here
        pass
    
    def pushStream(self):
        pass
    