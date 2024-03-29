# Generated by Django 2.2 on 2019-05-06 18:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190425_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documentation_score', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)])),
                ('completion_score', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15)])),
                ('creativity_score', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(20)])),
                ('purpose_score', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(25)])),
                ('understanding_score', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(30)])),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['front_end_id']},
        ),
        migrations.CreateModel(
            name='Project_Scoring',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Project', verbose_name='Project')),
                ('score', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Score', verbose_name='Score')),
            ],
        ),
    ]
