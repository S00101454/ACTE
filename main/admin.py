from django.contrib import admin

from .models import School
from .models import Student
from .models import Student_Project
from .models import Project 
from .models import Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Student_Project)
