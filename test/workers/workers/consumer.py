from workers.consumers.consumer import consumer
from workers.worker import worker
import unittest

class TestConsumer(unittest.TestCase):
    def test_connect(self):
        #TODO:Must be developed 
        cons = consumer("")
        self.assertTrue(cons.connect())
        self.assertFalse(cons.connect())

    def test_disconnect(self):
        #TODO:Must be developed 
        cons = consumer("")
        self.assertTrue(cons.disconnect())
        self.assertFalse(cons.disconnect())





#inject test class into unittest
if __name__ == '__main__':
    unittest.main()