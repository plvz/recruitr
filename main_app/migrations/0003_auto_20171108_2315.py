# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20171107_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant_position',
            name='applicant_ptr',
        ),
        migrations.RemoveField(
            model_name='applicant_position',
            name='position_ptr',
        ),
        migrations.RemoveField(
            model_name='applicant_skill',
            name='applicant_ptr',
        ),
        migrations.RemoveField(
            model_name='applicant_skill',
            name='skill_ptr',
        ),
        migrations.RemoveField(
            model_name='employee_skill',
            name='employee_ptr',
        ),
        migrations.RemoveField(
            model_name='employee_skill',
            name='skill_ptr',
        ),
        migrations.RemoveField(
            model_name='position_skill',
            name='position_ptr',
        ),
        migrations.RemoveField(
            model_name='position_skill',
            name='skill_ptr',
        ),
        migrations.AddField(
            model_name='applicant',
            name='apllicant_skills',
            field=models.ManyToManyField(to='main_app.Skill'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='applicant_positions',
            field=models.ManyToManyField(to='main_app.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_skills',
            field=models.ManyToManyField(to='main_app.Skill'),
        ),
        migrations.AddField(
            model_name='position',
            name='position_skills',
            field=models.ManyToManyField(to='main_app.Skill'),
        ),
        migrations.DeleteModel(
            name='Applicant_Position',
        ),
        migrations.DeleteModel(
            name='Applicant_Skill',
        ),
        migrations.DeleteModel(
            name='Employee_Skill',
        ),
        migrations.DeleteModel(
            name='Position_Skill',
        ),
    ]
