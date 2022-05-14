from lib.utils.config import config
from workers.consumers.consumer import consumer
from workers.producers.producer import producer
from workers.worker import workerInterface
from workers.publishers.publisher import publisher
from workers.analyzers.analyzer import analyzer


class WorkerFactory:

    @staticmethod
    def createWorker(workerType) -> workerInterface:
        match workerType:
            case config.PRODUCER_KEY:
                return producer("producerName")
            case config.CONSUMER_KEY:
                return consumer("consumerName")
            case config.PUBLISHER_KEY:
                return publisher("publisherName")
            case config.ANALYZER_KEY:
                return analyzer("analyzerName")                