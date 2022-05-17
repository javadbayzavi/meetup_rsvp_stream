import unittest

from lib.models.model import model


class TestModel(unittest.TestCase):

    def test_model(self):
        self.assertRaises(Exception, model(True))
        temp = model(12)
        self.assertEqual(temp.id , 12)
        temp2 = model()
        self.assertLess(temp2.id , 10000)
        self.assertGreater(temp2.id , 0)


#inject test class into unittest
if __name__ == '__main__':
    unittest.main()