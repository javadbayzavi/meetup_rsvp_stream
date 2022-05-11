from workers.worker import worker


class subscriber(worker):
    def __init__(self, broker) -> None:
        #TODO: some string checking before set broker config
        self.broker = broker
    
    def processMe(self):
        #Initiate subscriber process
        pass
