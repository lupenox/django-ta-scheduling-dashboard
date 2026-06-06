from django.contrib import admin
from django.urls import path

from project_app.views import (
    AssignmentsTAView,
    ContactInfoView,
    CourseManagementView,
    DashboardView,
    Home,
    InstructorCoursesView,
    LoginView,
    UserManagementView,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("manage-users/", UserManagementView.as_view(), name="user-management"),
    path("manage-courses/", CourseManagementView.as_view(), name="course-management"),
    path("instructor-courses/", InstructorCoursesView.as_view(), name="instructor-courses"),
    path("ta-assignments/", AssignmentsTAView.as_view(), name="ta-assignments"),
    path("contact-info/", ContactInfoView.as_view(), name="contact-info"),
]
