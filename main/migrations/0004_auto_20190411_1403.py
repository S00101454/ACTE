# Generated by Django 2.2 on 2019-04-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190411_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='school',
            name='school_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
    ]
