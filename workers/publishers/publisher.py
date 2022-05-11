from workers.worker import worker
from kafka import KafkaProducer


class publisher(worker):
    def __init__(self, broker) -> None:
        self.broker = broker
    
    def processMe(self):
        #publishing starts from here
        self.pushResult()
        pass
    
    def processMeAsync(self):
        #production starts from here
        pass
           
    def pushResult(self):
        pass
    