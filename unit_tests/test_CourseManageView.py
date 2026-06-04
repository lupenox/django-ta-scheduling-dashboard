from django.test import TestCase
from unittest.mock import Mock

from classes.CourseManagementPage import CourseManagement

mockClass = Mock()
mockTA = Mock()
mockSection = Mock()
mockInstructor = Mock()
mock = Mock()


class TestCourseManageView(TestCase):

    def setUp(self):
        mockClass.course_name = "361"
        mockClass.instructors = [mockInstructor]
        mockClass.tas = [mockTA]
        mockClass.sections = [mockSection]
        self.viewObject = CourseManagement()
        mock.courses = [mockClass]

    def test_deleteCourse(self):
        self.assertTrue(self.viewObject.deleteCourse("361"))
        self.assertNotIn(getCourse("361"), mock.courses)
        self.assertFalse(self.viewObject.deleteCourse("333"))

    def test_createCourse(self):
        self.assertTrue(self.viewObject.createCourse("351"))
        self.assertIn(getCourse("351"), mock.courses)
        self.assertFalse(self.viewObject.createCourse("361"))

    def test_listCourses(self):
        self.assertEqual(self.viewObject.listCourses(), mock.courses)

    def test_updateCourse(self):
        self.assertEqual(self.viewObject.updateCourse("361"), mockClass)
