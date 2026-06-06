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
        # Demo entry point while the legacy app is being refactored.
        return redirect("dashboard")


class DashboardView(View):
    def get(self, request):
        courses = Course.objects.prefetch_related("TAs", "sections", "instructor").all().order_by("name")
        return render(request, "dashboard.html", {"courses": courses})

    def post(self, request):
        return redirect("dashboard")


class UserManagementView(View):
    def get(self, request):
        return render(request, "userManagementView.html", self._context())

    def post(self, request):
        username = request.POST.get("username", "").strip()
        account_type = request.POST.get("account_type", AccountType.TA).strip()

        if not username:
            return render(request, "userManagementView.html", self._context("Staff name is required."))

        if account_type not in AccountType.values:
            return render(request, "userManagementView.html", self._context("Role must be TA, admin, or instructor."))

        staff_member, created = User.objects.get_or_create(
            username=username,
            defaults={"password": "demo-only", "accountType": account_type},
        )

        if not created and staff_member.accountType != account_type:
            staff_member.accountType = account_type
            staff_member.save()
            message = f"Updated {username}'s role."
        else:
            message = f"Added staff member {username}." if created else f"{username} already exists."

        return render(request, "userManagementView.html", self._context(message))

    def _context(self, message=None):
        context = {
            "users": User.objects.all().order_by("username"),
            "account_types": AccountType.choices,
        }
        if message:
            context["message"] = message
        return context


class CourseManagementView(View):
    def get(self, request):
        return render(request, "course_management.html", self._context())

    def post(self, request):
        course_name = request.POST.get("course_name", "").strip()
        instructor_username = request.POST.get("instructor", "").strip()

        if not course_name:
            return render(request, "course_management.html", self._context("Course name is required."))

        course, created = Course.objects.get_or_create(name=course_name)

        if instructor_username:
            instructor = get_object_or_404(User, username=instructor_username, accountType=AccountType.INSTRUCTOR)
            course.instructor.add(instructor)

        message = f"Created course {course.name}." if created else f"Updated course {course.name}."
        return render(request, "course_management.html", self._context(message))

    def _context(self, message=None):
        context = {
            "courses": Course.objects.prefetch_related("instructor").all().order_by("name"),
            "instructors": User.objects.filter(accountType=AccountType.INSTRUCTOR).order_by("username"),
        }
        if message:
            context["message"] = message
        return context


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
