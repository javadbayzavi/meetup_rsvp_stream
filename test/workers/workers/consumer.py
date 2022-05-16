from kafka import KafkaConsumer

from lib.utils.config import config
from workers.consumers.consumer import consumer
from workers.factory import WorkerFactory
import unittest

class TestAnalyzer(unittest.TestCase):
    consumer = None
    def setUp(self) -> None:
        self.consumer = WorkerFactory.createWorker(workerType = config.CONSUMER_KEY)
        return super().setUp()
         
    def test_broker(self):
        self.assertRaises(Exception , consumer())
        self.assertRaises(Exception , consumer(broker = ''))
        self.assertRaises(Exception , consumer(name = ''))
        self.assertRaises(Exception , consumer(name = 'Test' , broker = ''))
        self.assertRaises(Exception , consumer(name = 'Test' , broker = 'brokerTest'))
        self.assertIsInstance(consumer(name = 'Test' , broker = 'consumer'), type(consumer))

    def test_pullStream(self):
        self.assertIn("rsvp_id" , self.consumer.pullStream())
        self.assertTrue(self.consumer.actions.find('stream pulled') >= 0)

    def test_processMe(self):
        self.assertIsInstance(self.consumer.brokerCLient , type(KafkaConsumer))
        temp = self.consumer.extractMessage(None)
        self.assertEqual(len(temp) , 0)
        self.assertGreater(len(self.consumer.actions) , 0)
        self.assertTrue(self.consumer.actions.find('Message extracted') >= 0)
        self.assertRaises(Exception, self.consumer.dumpToDisk(None,'badfilename'))
        self.assertGreater(self.consumer._unhealthyrun , 0)  

    def tearDown(self) -> None:
        self.analyzer = None
        return super().tearDown()
        
#inject test class into unittest
if __name__ == '__main__':
    unittest.main()