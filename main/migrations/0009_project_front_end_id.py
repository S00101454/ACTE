# Generated by Django 2.2 on 2019-04-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190424_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='front_end_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]