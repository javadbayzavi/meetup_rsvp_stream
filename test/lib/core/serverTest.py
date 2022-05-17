
import unittest

from lib.core.server import server
from lib.utils.config import config


class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_brokerChecking(self):
        self.assertRaises(Exception , server.brokerChecking())
        self.assertFalse(server.brokerChecking(config.PRODUCER_TOPIC))
        self.assertFalse(server.brokerChecking(config.PUBLISHER_TOPIC))
        server.brokerConfigReset()
        self.assertTrue(server.brokerChecking(config.PRODUCER_TOPIC))
        self.assertTrue(server.brokerChecking(config.PUBLISHER_TOPIC))
        self.assertFalse(server.brokerChecking("Test"))





#inject test class into unittest
if __name__ == '__main__':
    unittest.main()