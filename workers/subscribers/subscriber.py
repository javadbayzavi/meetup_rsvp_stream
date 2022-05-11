from workers.worker import worker
from kafka import KafkaConsumer


class subscriber(worker):
    def __init__(self, broker) -> None:
        #TODO: some string checking before set broker config
        self.broker = broker
    
    def processMe(self):
        #Initiate subscriber process
        pass

    def processMeAsync(self):
        #production starts from here
        pass
       