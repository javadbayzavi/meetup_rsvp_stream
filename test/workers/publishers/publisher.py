from kafka import KafkaConsumer

from lib.utils.config import config
from workers.consumers.consumer import consumer
from workers.factory import WorkerFactory
from workers.analyzers.analyzer import analyzer
import unittest

class TestAnalyzer(unittest.TestCase):
    publisher = None
    def setUp(self) -> None:
        self.publisher = WorkerFactory.createWorker(workerType = config.PUBLISHER_KEY)
        return super().setUp()
         
    def test_broker(self):
        self.assertRaises(Exception , consumer())
        self.assertRaises(Exception , consumer(broker = ''))
        self.assertRaises(Exception , consumer(name = ''))
        self.assertRaises(Exception , consumer(name = 'Test' , broker = ''))
        self.assertRaises(Exception , consumer(name = 'Test' , broker = 'brokerTest'))
        self.assertIsInstance(analyzer(name = 'Test' , broker = 'publisher'), type(analyzer))

    def test_pullStream(self):
        self.assertIn("point" , self.publisher.pullStream())
        self.assertTrue(self.publisher.actions.find('stream pulled') >= 0)

    def test_processMe(self):
        self.assertIsInstance(self.publisher.brokerCLient , type(KafkaConsumer))
          
    def tearDown(self) -> None:
        self.analyzer = None
        return super().tearDown()
        
#inject test class into unittest
if __name__ == '__main__':
    unittest.main()