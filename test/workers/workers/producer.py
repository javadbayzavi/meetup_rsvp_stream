from kafka import KafkaProducer

import requests
from lib.utils.config import config
from workers.factory import WorkerFactory
from workers.producers.producer import producer
import unittest

class TestProducer(unittest.TestCase):
    producer = None
    def setUp(self) -> None:
        producer = WorkerFactory.createWorker(workerType = config.PRODUCER_KEY)
        return super().setUp()
    def test_broker(self):
        self.assertRaises(Exception , producer())
        self.assertRaises(Exception , producer(broker = ''))
        self.assertRaises(Exception , producer(name = ''))
        self.assertRaises(Exception , producer(name = 'Test' , broker = ''))
        self.assertRaises(Exception , producer(name = 'Test' , broker = 'brokerTest'))
        self.assertIsInstance(producer(name = 'Test' , broker = 'producer'), type(producer))

    def test_loadJson(self):
        self.assertIsNotNone(config.MEETUP_RSVP_ENDPOINT)
        self.assertIsNotNone(requests.get(config.MEETUP_RSVP_ENDPOINT),"Failed server fetch")
        self.assertIsNotNone(self.producer.loadJson(), "Load Json from remote server failed")
        self.assertIn("rsvp_id" , self.producer.loadJson())

    def test_processMe(self):
        self.assertIsInstance(self.producer.brokerCLient , type(KafkaProducer))
        self.producer.pushStream(None)
        self.assertGreater(len(self.producer.actions) , 0)
        self.assertTrue(self.producer.actions.find('Stream pushed') > 0)
    
    def tearDown(self) -> None:
        self.producer = None
        return super().tearDown()
        
#inject test class into unittest
if __name__ == '__main__':
    unittest.main()