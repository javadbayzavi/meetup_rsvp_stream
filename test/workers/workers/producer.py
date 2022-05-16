from hashlib import new
from unicodedata import name
from workers.producers.producer import producer
import unittest

class TestProducer(unittest.TestCase):
    def test_broker(self):
        self.assertRaises(Exception , producer())
        self.assertRaises(Exception , producer(broker = ''))
        self.assertRaises(Exception , producer(name = ''))
        self.assertRaises(Exception , producer(name = 'Test' , broker = ''))
        self.assertRaises(Exception , producer(name = 'Test' , broker = 'brokerTest'))
        self.assertIsInstance(producer(name = 'Test' , broker = 'producer'), type(producer))

    def test_loadJson(self):




#inject test class into unittest
if __name__ == '__main__':
    unittest.main()