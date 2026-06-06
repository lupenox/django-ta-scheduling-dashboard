from django.shortcuts import redirect, render
from django.views import View


class Home(View):
    def get(self, request):
        """Redirect the root URL to the login page."""
        return redirect("login")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        # TODO: Replace placeholder behavior with real authentication logic.
        return redirect("dashboard")


class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html")

    def post(self, request):
        return redirect("dashboard")


class UserManagementView(View):
    def get(self, request):
        return render(request, "userManagementView.html")

    def post(self, request):
        return redirect("user-management")


class CourseManagementView(View):
    def get(self, request):
        return render(request, "course_management.html")

    def post(self, request):
        return redirect("course-management")


class InstructorCoursesView(View):
    def get(self, request):
        return render(request, "instructor_courses.html")

    def post(self, request):
        return redirect("instructor-courses")


class AssignmentsTAView(View):
    def get(self, request):
        return render(request, "ta_assignment.html")

    def post(self, request):
        return redirect("ta-assignments")


class ContactInfoView(View):
    def get(self, request):
        return render(request, "contact_info.html")

    def post(self, request):
        return redirect("contact-info")
