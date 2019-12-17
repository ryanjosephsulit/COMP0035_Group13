from unittest import TestCase

from Lesson import Lesson


class TestLesson(TestCase):

    def setUp(self):
        self.lesson = Lesson()

    def test_scheduleLocation(self):
        location = "UCL Science Library"
        ScheduledLesson.scheduleLessonLocation(v)
        ScheduleLocation_check = (self.lesson.scheduleLessonLocation(location))
        self.assertMultiLineEqual(location, ScheduleLocation_check)

    def test_scheduleTime(self):
        time = datetime.date.today()
        ScheduledLesson.scheduleLessonTime(t)
        ScheduleTime_check = (self.lesson.scheduleLessonTime(time))
        self.assertMultiLineEqual(time, ScheduleTime_check)

    def test_scheduleFormat(self):
        format = "In-Person Meeting"
        ScheduledLesson.scheduleLessonFormat(f)
        ScheduleFormat_check = (self.lesson.scheduleLessonFormat(format))
        self.assertMultiLineEqual(format, ScheduleFormat_check)


    def test_scheduleStatus(self):
        status = "Upcoming"
        ScheduledLesson.scheduleLessonStatus(s)
        ScheduleStatus_check = (self.lesson.scheduleLessonLocation(status))
        self.assertMultiLineEqual(status, ScheduleStatus_check)
