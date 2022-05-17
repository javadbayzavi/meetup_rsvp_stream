import unittest

from schemas.meetup.rsvp import rsvp


class TestRSVP(unittest.TestCase):

    def test_model(self):
        self.assertRaises(Exception, rsvp(True))
        temp = rsvp(12)
        self.assertEqual(temp.id , 12)
        temp2 = rsvp()
        self.assertLess(temp2.id , 10000)
        self.assertGreater(temp2.id , 0)


#inject test class into unittest
if __name__ == '__main__':
    unittest.main()