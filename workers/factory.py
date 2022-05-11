from email.policy import default
from workers.consumers.consumer import consumer
from workers.producers.producer import producer
from workers.worker import workerInterface


class WorkerFactory:
    def createWorker(workerType) -> workerInterface:
        match workerType:
            case "producer":
                return producer("")
            case "consumer":
                return consumer("")
            #TODO: add a default instance to handle incorrect workertype input
    
    def createAsyncWorker(workerType):
        #TODO: incorporate the code with threads
        pass