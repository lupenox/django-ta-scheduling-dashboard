from unittest import TestCase
from classes import LoginView, TA_AssignmentView

class AuthenticationTests(TestCase):
    def setUp(self):
        # Store user in an instance variable to be accessible across methods if needed
        self.user = LoginView(name="user1", password="pass1")

    def test_authenticate_user_valid(self):
        user = LoginView.authenticateUser("user1", "pass1")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "user1")

    def test_authenticate_user_invalid(self):
        # Test for invalid credentials
        user = LoginView.authenticateUser("user1", "wrongpass")
        self.assertIsNone(user)

class TATests(TestCase):
    def setUp(self):
        self.instructor = TA_AssignmentView(name="instructor", password="pass123")
        self.ta = TA_AssignmentView(name="ta1", password="pass123")
        self.course = TA_AssignmentView(name="Algebra", instructor=self.instructor)
        self.assignment = TA_AssignmentView(course=self.course, ta=self.ta)

    def test_get_ta_assignments(self):
        assignments = TA_AssignmentView.getTAAssignments("ta1")
        self.assertEqual(len(assignments), 1)
        self.assertEqual(assignments[0].course.name, "Algebra")
