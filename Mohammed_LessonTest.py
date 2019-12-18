import unittest
from unittest import TestCase
import datetime
from Lesson import Lesson


class TestLesson(TestCase):

    def setUp(self):
        self.Lesson = Lesson

    def test_scheduleLocation(self):
        v = "UCL Science Library"
        location = "UCL Science Library"
        Lesson.scheduleLessonLocation(v)
        ScheduleLocation_check = (Lesson.scheduleLessonLocation(v))
        self.assertEqual(location, ScheduleLocation_check)

    def test_scheduleTime(self):
        timetoday = datetime.date.today()
        Lesson.timing(self, t)
        ScheduleTime_check = (self.Lesson.timing(t))
        self.assertEqual(timetoday, ScheduleTime_check)

    def test_scheduleFormat(self):
        format = "In-Person Meeting"
        Lesson.scheduleLessonFormat(self, f)
        ScheduleFormat_check = (self.Lesson.scheduleLessonFormat(f))
        self.assertEqual(format, ScheduleFormat_check)


    def test_scheduleStatus(self):
        status = "Upcoming"
        Lesson.scheduleLessonStatus(self, s)
        ScheduleStatus_check = (self.Lesson.scheduleLessonLocation(s))
        self.assertEqual(status, ScheduleStatus_check)

if __name__ == '__main__':
    Lesson = Lesson()
    v = "UCL Science Library"
    t = datetime.date.today()
    f = "In-Person Meeting"
    s = "Upcoming"
    Lesson.scheduleLessonLocation(v)
    Lesson.scheduleLessonTime(t)
    Lesson.scheduleLessonFormat(f)
    Lesson.scheduleLessonStatus(s)
    unittest.main()