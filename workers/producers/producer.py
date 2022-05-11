from workers.worker import worker
from kafka import KafkaProducer

class producer(worker):
    def __init__(self, broker) -> None:
        self.broker = broker
    
    def processMe(self):
        #production starts from here
        pass
    
    def pushStream(self):
        pass

    def processMeAsync(self):
        #production starts from here
        pass
       
    def __produce(self) -> str:
        #TODO: stub method to generate input rsvp stream
        return "Sample string"