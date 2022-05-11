from workers.publishers.publisher import publisher
from workers.worker import worker
import unittest


class TestPublisher(unittest.TestCase):
    def test_connect(self):
        #TODO:Must be developed 
        pubs = publisher("")
        self.assertTrue(pubs.connect())
        self.assertFalse(pubs.connect())

    def test_disconnect(self):
        #TODO:Must be developed 
        pubs = publisher("")
        self.assertTrue(pubs.disconnect())
        self.assertFalse(pubs.disconnect())






#inject test class into unittest
if __name__ == '__main__':
    unittest.main()