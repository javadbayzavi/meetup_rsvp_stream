from email.policy import default
from workers.consumers.consumer import consumer
from workers.producers.producer import producer
from workers.worker import workerInterface
from workers.publishers.publisher import publisher
from workers.subscribers.subscriber import subscriber


class WorkerFactory:

    @staticmethod
    def createWorker(workerType) -> workerInterface:
        match workerType:
            case "producer":
                return producer("")
            case "consumer":
                return consumer("")
            case "publisher":
                return producer("")
            case "subscriber":
                return consumer("")                