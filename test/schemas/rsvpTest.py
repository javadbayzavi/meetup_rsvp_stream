import unittest

from schemas.meetup.rsvp import rsvp


class TestRSVP(unittest.TestCase):

    def test_rsvp(self):
        self.assertRaises(Exception, rsvp(True))
        temp = {
            "group_name" : "group",
            "group_city" : "London",
            "group_country" : "uk",
            "group_lon" : "12.0",
            "group_lat" : "0.12",
            "group_urlname" : "http://www.abc.org",
            "group_state" : "lnd"
        }
        rsvp_tem = rsvp(12,"Visible","Test","2","1234567890",temp)
        self.assertEqual(rsvp_tem.id , 12)
        self.assertEqual(rsvp_tem.group_name , "London")
        self.assertEqual(rsvp_tem.group_city , "uk")
        self.assertEqual(rsvp_tem.group_lon , "12.0")
        self.assertEqual(rsvp_tem.group_lat , "0.12")
        self.assertEqual(rsvp_tem.urlname , "http://www.abc.org")
        self.assertEqual(rsvp_tem.group_state , "lnd")


#inject test class into unittest
if __name__ == '__main__':
    unittest.main()