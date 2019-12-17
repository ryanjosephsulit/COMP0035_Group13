#COMP0035: Systems Engineering - Individual Coursework

#Mohammed Hasan - Student Number 17014291

#Lesson class
# this file exists for the purpose of demonstration
import datetime

class Lesson:
    def __init__(self):
        self.status = []
        self.type = []
        self.datetime = []
        self.location = []
    def scheduleLessonLocation(self, Venue):
            self.location = Venue

    def scheduleLessonTime(self, Time):
            self.datetime = Time

    def scheduleLessonFormat(self, Format):
        self.type = Format

    def scheduleLessonStatus(self, Status):
            self.status = Status


ScheduledLesson = Lesson()
v = "UCL Science Library"
t = datetime.date.today()
f = "In-Person Meeting"
s = "Upcoming"
ScheduledLesson.scheduleLessonLocation(v)
ScheduledLesson.scheduleLessonTime(t)
ScheduledLesson.scheduleLessonFormat(f)
ScheduledLesson.scheduleLessonStatus(s)
