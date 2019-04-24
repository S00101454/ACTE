from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=192)
    address = models.CharField(max_length=192)
    students_attending = models.PositiveIntegerField(null=True)
    chaperones_attending = models.PositiveIntegerField()
    teachers_attending = models.PositiveIntegerField()
    drivers_attending = models.PositiveIntegerField()
    amount_paid = models.DecimalField(max_digits=15,decimal_places=2, null=True)
    contact_name = models.CharField(max_length = 192)
    contact_email = models.CharField(max_length = 192)
    contact_primary_phone = models.CharField(max_length = 64)
    contact_alternate_phone = models.CharField(max_length = 66, null=True)

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
    front_end_id = models.PositiveIntegerField(null=True)
    
    school = models.ForeignKey(School,verbose_name="School", on_delete=models.CASCADE)
    category = models.ForeignKey(Category,verbose_name="Category", on_delete=models.CASCADE)
    name = models.CharField (max_length=192)
    level = models.PositiveIntegerField(validators=[MaxValueValidator(5),])
    is_group = models.BooleanField()
    score = models.SmallIntegerField()

    def __str__(self):
        return (self.name)


class Student_Project(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student,verbose_name="Student", on_delete=models.CASCADE)
    project = models.ForeignKey(Project,verbose_name="Project", on_delete=models.CASCADE)

    def __str__(self):
        return (self.student + ' : ' + self.project)

