from django.contrib import admin

from project_app.models import ContactInfo, Course, Section, User


admin.site.register(ContactInfo)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(User)
