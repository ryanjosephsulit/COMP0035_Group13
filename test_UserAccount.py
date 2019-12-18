from unittest import TestCase
import unittest
from UserAccount import UserAccount

class TestUserAccount(TestCase):

    def setUp(self):
        self.user = UserAccount

    def test_edit_location(self):
        location = "Africa";
        location_check = (self.user.edit_location(location))
        self.assertMultiLineEqual(location, location_check)

        #self.assertMultiLineEqual(location, location_check)
if __name__ == '__main__':

    unittest.main()
