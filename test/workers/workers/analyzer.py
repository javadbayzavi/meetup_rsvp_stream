from kafka import KafkaProducer

from lib.utils.config import config
from workers.factory import WorkerFactory
from workers.analyzers.analyzer import analyzer
import unittest

class TestAnalyzer(unittest.TestCase):
    analyzer = None
    def setUp(self) -> None:
        self.analyzer = WorkerFactory.createWorker(workerType = config.ANALYZER_KEY)
        return super().setUp()
         
    def test_broker(self):
        self.assertRaises(Exception , analyzer())
        self.assertRaises(Exception , analyzer(broker = ''))
        self.assertRaises(Exception , analyzer(name = ''))
        self.assertRaises(Exception , analyzer(name = 'Test' , broker = ''))
        self.assertRaises(Exception , analyzer(name = 'Test' , broker = 'brokerTest'))
        self.assertIsInstance(analyzer(name = 'Test' , broker = 'analyzer'), type(analyzer))

    def test_loadFromDisk(self):
        self.assertIn("group_city" , self.analyzer.loadFromDisk())

    def test_processMe(self):
        self.assertIsInstance(self.analyzer.brokerCLient , type(KafkaProducer))
        self.analyzer.pushResult(None)
        self.assertGreater(len(self.analyzer.actions) , 0)
        self.assertTrue(self.analyzer.actions.find('Stream pushed') > 0)
    
    def tearDown(self) -> None:
        self.analyzer = None
        return super().tearDown()
        
#inject test class into unittest
if __name__ == '__main__':
    unittest.main()