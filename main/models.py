from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=192)
    address = models.CharField(max_length=192)
    students_attending = models.PositiveIntegerField(blank=True,null=True)
    chaperones_attending = models.PositiveIntegerField()
    teachers_attending = models.PositiveIntegerField()
    drivers_attending = models.PositiveIntegerField()
    amount_paid = models.DecimalField(max_digits=15,decimal_places=2, blank=True,null=True)
    contact_name = models.CharField(max_length = 192)
    contact_email = models.CharField(max_length = 192)
    contact_primary_phone = models.CharField(max_length = 64)
    contact_alternate_phone = models.CharField(max_length = 66, blank=True,null=True)

    def __str__(self):
        return (self.school_name)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length = 192)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return (self.category_name)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School,verbose_name="School", on_delete=models.CASCADE)
    name_first = models.CharField(max_length=192)
    name_last = models.CharField(max_length=192)
    level = models.PositiveSmallIntegerField(validators = [MaxValueValidator(5),])
    is_testing = models.BooleanField()

    def __str__(self):
        return (self.name_first + ' ' + self.name_last)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    front_end_id = models.PositiveIntegerField(blank=True,null=True)
    
    school = models.ForeignKey(School,verbose_name="School", on_delete=models.CASCADE)
    category = models.ForeignKey(Category,verbose_name="Category", on_delete=models.CASCADE)
    name = models.CharField (max_length=192)
    level = models.PositiveIntegerField(validators=[MaxValueValidator(5),])
    is_group = models.BooleanField()
    score = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["front_end_id"]
    def __str__(self):
        return (self.name)

class Student_Project(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,verbose_name="Student", on_delete=models.CASCADE)
    project = models.ForeignKey(Project,verbose_name="Project", on_delete=models.CASCADE)

    def __str__(self):
        return (self.student + ' : ' + self.project)

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    documentation_score = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(10),])
    completion_score = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(15),])
    creativity_score = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(20),])
    purpose_score = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(25),])
    understanding_score = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(30),])
    comments = models.TextField(max_length=2000, blank=True, null=True)

class Project_Scoring(models.Model):
    unique_together = (('project', 'judge'),)
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.PROTECT)
    score = models.ForeignKey(Score, verbose_name="Score", null=True, on_delete=models.SET_NULL)
    judge = models.ForeignKey(User, verbose_name="Judge", null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return (self.id)