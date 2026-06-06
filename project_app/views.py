from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from project_app.models import AccountType, Course, Section, User


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
        courses = Course.objects.prefetch_related("TAs", "sections", "instructor").all()
        return render(request, "dashboard.html", {"courses": courses})

    def post(self, request):
        return redirect("dashboard")


class UserManagementView(View):
    def get(self, request):
        users = User.objects.all().order_by("username")
        return render(request, "userManagementView.html", {"users": users})

    def post(self, request):
        return redirect("user-management")


class CourseManagementView(View):
    def get(self, request):
        courses = Course.objects.all().order_by("name")
        return render(request, "course_management.html", {"courses": courses})

    def post(self, request):
        return redirect("course-management")


class InstructorCoursesView(View):
    def get(self, request):
        courses = Course.objects.prefetch_related("instructor").all().order_by("name")
        return render(request, "instructor_courses.html", {"courses": courses})

    def post(self, request):
        return redirect("instructor-courses")


class AssignmentsTAView(View):
    def get(self, request):
        context = self._assignment_context()
        return render(request, "ta_assignment.html", context)

    def post(self, request):
        ta_username = request.POST.get("TASelect")
        course_name = request.POST.get("CourseSelect")
        section_number = request.POST.get("lab_section")

        ta = get_object_or_404(User, username=ta_username, accountType=AccountType.TA)
        course = get_object_or_404(Course, name=course_name)
        section, _created = Section.objects.get_or_create(number=section_number, course=course)

        section.ta = ta
        section.course = course
        section.save()

        course.TAs.add(ta)
        course.sections.add(section)

        context = self._assignment_context(
            message=f"Assigned {ta.username} to {course.name}, section {section.number}."
        )
        return render(request, "ta_assignment.html", context)

    def _assignment_context(self, message=None):
        context = {
            "courses": Course.objects.prefetch_related("TAs", "sections", "instructor").all().order_by("name"),
            "TAs": User.objects.filter(accountType=AccountType.TA).order_by("username"),
            "sections": Section.objects.select_related("course", "ta").all().order_by("course__name", "number"),
        }
        if message:
            context["message"] = message
        return context


class ContactInfoView(View):
    def get(self, request):
        return render(request, "contact_info.html")

    def post(self, request):
        return redirect("contact-info")
