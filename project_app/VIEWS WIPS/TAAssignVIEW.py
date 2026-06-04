from django.shortcuts import render, redirect
from django.views import View

from classes.course_class import CourseClass
from project_app.models import User, Course, AccountType, Section


class assignmentsTAView(View):
    def get(self, request):
        courses = Course.objects.all()
        tas = User.objects.filter(accountType=AccountType.TA)
        sections = Section.objects.all()
        return render(request, 'ta_assignment.html', {'courses': courses, 'tas': tas, 'sections': sections})

    def post(self, request):
        ta_username = request.POST.get('TASelect')
        course_name = request.POST.get('CourseSelect')
        section_number = request.POST.get('lab_section')

        ta = User.objects.get(username=ta_username)
        section = Section.objects.get_or_create(number=section_number)
        course = Course.objects.get(name=course_name)

        temp_course_inst = CourseClass()
        temp_course_inst.add_ta(ta)
        temp_course_inst.add_section(section)

        temp_course_inst.add_ta(ta_username)
        temp_course_inst.add_section(section_number)

        course.TAs.set(temp_course_inst.tas)
        course.sections.set(temp_course_inst.sections)

        course.save()

        return redirect('dashboard')
