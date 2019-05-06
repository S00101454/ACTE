from django.contrib import admin

from .models import School, Student, Student_Project,Project, Category, Score, Project_Scoring

# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Score)
