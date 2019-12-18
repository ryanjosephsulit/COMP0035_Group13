#COMP0035: Systems Engineering - Individual Coursework
#Mohammed Hasan - Student Number 17014291

#Lesson class
# this file exists for the purpose of demonstration
import datetime

class Lesson:
    def __init__(self):
        self.status = None
        self.type = None
        self.timing = None
        self.location = None
    def scheduleLessonLocation(self, v):
            self.location = v

    def scheduleLessonTime(self, t):
            self.timing = t

    def scheduleLessonFormat(self, f):
        self.type = f

    def scheduleLessonStatus(self, s):
            self.status = s


if __name__ == '__main__':
    Lesson = Lesson()
    v = "Tokyo"
    t = datetime.date.today()
    f = "In-Person Meeting"
    s = "Upcoming"
    Lesson.scheduleLessonLocation(v)
    Lesson.scheduleLessonTime(t)
    Lesson.scheduleLessonFormat(f)
    Lesson.scheduleLessonStatus(s)
    print(Lesson.location, Lesson.timing, Lesson.type, Lesson.status)
