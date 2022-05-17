  
import unittest

import requests
from lib.core.schedulerEngine import schedulerEngine

from lib.utils.config import config
from workers.factory import WorkerFactory
from workers.producers.producer import producer


class TestWebServer(unittest.TestCase):
    scheduler = None
    def setUp(self) -> None:
        self.scheduler = schedulerEngine()
        return super().setUp()

    def tearDown(self) -> None:
        self.webserver = None
        return super().tearDown()

    def test_schedule(self):
        self.assertRaises(Exception, self.scheduler.schedule(None)) 
        t = WorkerFactory.createWorker(config.PRODUCER_KEY),type(producer)
        self.scheduler.schedule(t)
        self.assertTrue(self.scheduler.getProcessPoolCount() == 1)
        self.assertTrue(self.scheduler.getProcessProfileCount() == 1)

    def safeTerminate(self):
        t = WorkerFactory.createWorker(config.PRODUCER_KEY),type(producer)
        self.scheduler.schedule(t)
        self.assertTrue(self.scheduler.getProcessPoolCount() == 1)
        self.assertTrue(self.scheduler.getProcessProfileCount() == 1)
        self.scheduler.safeTerminate(t)
        self.assertTrue(self.scheduler.getProcessPoolCount() == 0)
        self.assertTrue(self.scheduler.getProcessProfileCount() == 0)        






#inject test class into unittest
if __name__ == '__main__':
    unittest.main()