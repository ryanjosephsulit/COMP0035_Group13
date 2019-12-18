#Testing the unittest for scheduling lesson location
# by giving a value of None to v, and the NotEqual assertation, we can test this method

from unittest import TestCase
import unittest
from Mohammed_Lesson import Lesson

class TestLesson(TestCase):

    def setUp(self):
        self.Lesson = Lesson

    def testScheduleLessonLocation(self):
        v = None;
        location_check = (self.Lesson.scheduleLessonLocation(self, v))
        self.assertNotEqual(v, location_check)

if __name__ == '__main__':
    unittest.main()
