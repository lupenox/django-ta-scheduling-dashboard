from django.test import TestCase
from django.urls import reverse

from project_app.models import AccountType, Course, Section, User


class PageSmokeTests(TestCase):
    def test_main_pages_load(self):
        route_names = [
            "login",
            "dashboard",
            "user-management",
            "course-management",
            "ta-assignments",
            "contact-info",
        ]

        for route_name in route_names:
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))
                self.assertEqual(response.status_code, 200)


class StaffManagementTests(TestCase):
    def test_create_staff_member(self):
        response = self.client.post(
            reverse("user-management"),
            {
                "username": "jordan_ta",
                "account_type": AccountType.TA,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            User.objects.filter(
                username="jordan_ta",
                accountType=AccountType.TA,
            ).exists()
        )


class CourseManagementTests(TestCase):
    def test_create_course_with_instructor(self):
        instructor = User.objects.create(
            username="prof_smith",
            password="demo-only",
            accountType=AccountType.INSTRUCTOR,
        )

        response = self.client.post(
            reverse("course-management"),
            {
                "course_name": "CS 101",
                "instructor": instructor.username,
            },
        )

        self.assertEqual(response.status_code, 200)

        course = Course.objects.get(name="CS 101")
        self.assertIn(instructor, course.instructor.all())


class SchedulingWorkflowTests(TestCase):
    def test_assign_ta_to_course_section(self):
        ta = User.objects.create(
            username="ta_jordan",
            password="demo-only",
            accountType=AccountType.TA,
        )
        course = Course.objects.create(name="CS 101")

        response = self.client.post(
            reverse("ta-assignments"),
            {
                "TASelect": ta.username,
                "CourseSelect": course.name,
                "lab_section": "801",
            },
        )

        self.assertEqual(response.status_code, 200)

        section = Section.objects.get(number="801", course=course)
        self.assertEqual(section.ta, ta)
        self.assertIn(ta, course.TAs.all())
        self.assertIn(section, course.sections.all())
