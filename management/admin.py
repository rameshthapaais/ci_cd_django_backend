from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(StudentMark)
