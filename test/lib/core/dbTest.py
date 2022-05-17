
import unittest

from lib.core.db import dbEngine


class TestDb(unittest.TestCase):
    db = None
    def setUp(self) -> None:
        self.db = dbEngine()
        return super().setUp()

    def tearDown(self) -> None:
        self.db = None
        return super().tearDown()

    def test_trendDb(self):
        testSql = "Select * from city_trend"
        self.db.exeuteQuery(testSql)
        self.assertIsNotNone(self.db.resu)
        




#inject test class into unittest
if __name__ == '__main__':
    unittest.main()