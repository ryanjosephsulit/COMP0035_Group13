from unittest import TestCase

from UserAccount import UserAccount

class TestUserAccount(TestCase):

    def setUp(self):
        # Create a test User_Account
        self.test_user = UserAccount

        # Set an initial test location to "London"
        self.test_user.set_location = "London"

    def test_edit_location(self):

        #Set new test location to "Manchester"
        location = "Manchester";

        #Calls the edit_location method and changes location to "Manchester"
        location_check = (self.test_user.edit_location(location));

        #Assert that new edited location is equal
        self.assertMultiLineEqual(location, location_check)

    def test_edit_location_false(self):
        #Expected location to be "Manchester"
        expected_location = "Manchester"

        #Assertion that current location is not equal
        self.assertMultiLineEqual(expected_location, self.test_user.set_location)