from re import sub
from workers.subscribers.subscriber import subscriber
from workers.worker import worker
import unittest


class TestSubscriber(unittest.TestCase):
    def test_connect(self):
        #TODO:Must be developed 
        subs = subscriber("")
        self.assertTrue(subs.connect())
        self.assertFalse(subs.connect())

    def test_disconnect(self):
        #TODO:Must be developed 
        subs = subscriber("")
        self.assertTrue(subs.disconnect())
        self.assertFalse(subs.disconnect())








#inject test class into unittest
if __name__ == '__main__':
    unittest.main()