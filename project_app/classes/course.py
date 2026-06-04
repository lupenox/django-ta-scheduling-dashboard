from project_app.classes.section import CourseSection
from project_app.models import Course,User,Section


class CourseClass:

    def __init__(self, name, instructors, ta, sections):
        self.name = name
        self.instructors = instructors
        self.ta = ta
        self.sections = sections

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_instructors(self, instructors):
        self.instructors = instructors

    def get_instructors(self):
        return self.instructors

    def addTAs(self, ta_ID):
        if isinstance(ta_ID, User) & ta_ID.accountType == "TA":
            self.ta.append(ta_ID)
            return True
        else:
            return False

    def removeTA(self, ta_ID):
        if isinstance(ta_ID, User) & ta_ID.accountType == "TA":
            self.ta.remove(ta_ID)
            return True
        else:
            return False

    def addSection(self, section_ID):
        if isinstance(section_ID, CourseSection):
            self.sections.append(section_ID)
            return True
        else:
            return False

    def removeSection(self, section_ID):
        if isinstance(section_ID, CourseSection):
            self.sections.remove(section_ID)
            return True
        else:
            return False

