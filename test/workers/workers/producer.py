from workers.producers.producer import producer
from workers.worker import worker
import unittest

class TestProducer(unittest.TestCase):
    def test_connect(self):
        #TODO:Must be developed 
        prod = producer("")
        self.assertTrue(prod.connect())
        self.assertFalse(prod.connect())

    def test_disconnect(self):
        #TODO:Must be developed 
        prod = producer("")
        self.assertTrue(prod.disconnect())
        self.assertFalse(prod.disconnect())





#inject test class into unittest
if __name__ == '__main__':
    unittest.main()