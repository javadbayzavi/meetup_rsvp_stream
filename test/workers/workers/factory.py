from lib.utils.config import config
from workers.consumers.consumer import consumer
from workers.producers.producer import producer
from workers.publishers.publisher import publisher
from workers.analyzers.analyzer import analyzer
from workers.factory import WorkerFactory
import unittest


class TestWorkerFactory(unittest.TestCase):

    def test_createWorker(self):
        self.assertIsInstance(WorkerFactory.createWorker(config.PRODUCER_KEY),type(producer))
        self.assertIsInstance(WorkerFactory.createWorker(config.CONSUMER_KEY),type(consumer))
        self.assertIsInstance(WorkerFactory.createWorker(config.PUBLISHER_KEY),type(publisher))
        self.assertIsInstance(WorkerFactory.createWorker(config.ANALYZER_KEY),type(analyzer))


#inject test class into unittest
if __name__ == '__main__':
    unittest.main()