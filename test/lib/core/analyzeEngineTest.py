
import unittest

from lib.core.analyzeEngine import analyzerEngine


class TestAnalyzerEngine(unittest.TestCase):
    engien = None
    def setUp(self) -> None:
        self.engien = analyzerEngine()
        return super().setUp()

    def tearDown(self) -> None:
        self.engien = None
        return super().tearDown()

    def test_trendAnaylze(self):
        self.assertListEqual(self.engien.analyzeTrend(), [])
        testdata = list(
            {
                "name" : "London",
                "group_lon" : "-12.4",
                "group_lat" : "0.2",
            },{
                "name" : "London",
                "group_lon" : "-12.4",
                "group_lat" : "0.2",
            },{
                "name" : "Paris",
                "group_lon" : "-12.4",
                "group_lat" : "2.2",
            }
        )
        res = list(
            {
                "name" : "London",
                "group_lon" : "-12.4",
                "group_lat" : "0.2",
                "point" : 2
            },{
                "name" : "Paris",
                "group_lon" : "-12.4",
                "group_lat" : "2.2",
                "point" : 1
            }
        )
        self.assertListEqual(self.engien.analyzeTrend(testdata),res)
        self.assertEqual(self.engien.analyzeTrend(testdata) , len(res))




#inject test class into unittest
if __name__ == '__main__':
    unittest.main()