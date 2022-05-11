from workers.worker import worker
from kafka import KafkaConsumer


class consumer(worker):
    def __init__(self, broker) -> None:
        #TODO: some string checking before set broker config
        self.broker = broker
    
    def processMe(self):
        #Initiate consumer process
        pass

    def processMeAsync(self):
        #production starts from here
        pass
       