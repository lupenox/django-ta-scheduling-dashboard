from django.test import TestCase
from classes.course import CourseClass


class TestCourseClass(TestCase):
    class TestAddCourseName(TestCase):
        def setUp(self):
            self.course = CourseClass()

        def test_base(self):
            self.course.set_course_name("test")
            self.assertEqual(self.course.course_name, "test")

        def test_no_arg(self):
            with self.assertRaises(TypeError):
                self.course.set_course_name()

        def test_invalid_type(self):
            with self.assertRaises(TypeError):
                self.course.set_course_name(1)
