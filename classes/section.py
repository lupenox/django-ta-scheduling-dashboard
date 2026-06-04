from project_app.models import Section


class CourseSection:
    def __init__(self, name, course, ta):
        self.name = name
        self.course = course
        self.ta = ta

    def removeTA(self):
        self.ta = None
        if self.ta == None:
            return true
        else:
            return false

    def setTA(self, ta):
        self.ta = ta
        if self.ta == ta:
            return true
        else:
            return false
