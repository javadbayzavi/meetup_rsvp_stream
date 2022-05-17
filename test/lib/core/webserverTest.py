  
import unittest

import requests

from lib.core.webserver import serverManager, webserver
from lib.utils.config import config


class TestWebServer(unittest.TestCase):
    webserver = None
    serverman = None
    def setUp(self) -> None:
        self.webserver = webserver()
        self.serverman = serverManager()
        return super().setUp()

    def tearDown(self) -> None:
        self.webserver = None
        return super().tearDown()

    def test_loadJson(self):
        temp = self.webserver.loadJson()
        self.assertIsNotNone(temp)
        self.assertEqual(len(temp) , 1)
        self.assertTrue(temp.find("rsvp_id") >= 0 )

    def test_loadResult(self):
        temp = self.webserver.loadResult()
        self.assertGreater(len(temp), 0)
        self.assertTrue(temp.find("name") > 0)
    
    def test_serverUp(self):
        self.serverman.start()
        req  = requests.get(config.MEETUP_RSVP_ENDPOINT)
        res  = requests.get(config.TREND_ENDPOINT)
        self.assertTrue(req.text.find("rsvp_id") > 0)
        self.assertTrue(res.text.find("name") > 0)




#inject test class into unittest
if __name__ == '__main__':
    unittest.main()