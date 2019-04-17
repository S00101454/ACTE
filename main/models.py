from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Student(models.Model):
    name_first = models.CharField(max_length=192)
    name_last = models.CharField(max_length=192)
    level = models.PositiveSmallIntegerField(validators = [MaxValueValidator(5),])
    school_id = models.PositiveIntegerField()
    is_testing = models.BooleanField()

    def __str__(self):
        return (self.name_first + ' ' + self.name_last)

class Project(models.Model):
    school_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    project_name = models.TextField()
    level = models.PositiveIntegerField(validators=[MaxValueValidator(5),])
    is_group = models.BooleanField()
    score = models.SmallIntegerField()

    def __str__(self):
        return (self.project_name)

class School(models.Model):
    school_name = models.CharField(max_length=192)
    address = models.CharField(max_length=192)
    students_attending = models.PositiveIntegerField()
    chaperones_attending = models.PositiveIntegerField()
    teachers_attending = models.PositiveIntegerField()
    drivers_attending = models.PositiveIntegerField()
    amount_paid = models.DecimalField(max_digits=15,decimal_places=2)
    contact_name = models.CharField(max_length = 192)
    contact_email = models.CharField(max_length = 192)
    contact_primary_phone = models.CharField(max_length = 64)
    contact_alternate_phone = models.CharField(max_length = 66)

    def __str__(self):
        return (self.school_name)

class Category(models.Model):
    category_name = models.CharField(max_length = 192)

    def __str__(self):
        return (self.category_name)

class Student_Project(models.Model):
    project_id = models.PositiveIntegerField()
    student_id = models.PositiveIntegerField()

    def __str__(self):
        return (self.student_id + ' : ' + self.project_id)

