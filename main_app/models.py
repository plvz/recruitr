# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    number_position = models.DecimalField(max_digits=5, decimal_places=0)
    description = models.TextField()

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=100)
    field = models.CharField(max_length=100)

class Position_Skill(Position, Skill):
    pass

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    '''phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
                                '''
    seniority = models.DecimalField(max_digits=3, decimal_places=0)

class Employee_Skill(Employee, Skill):
    pass

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    angel_url = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

class Applicant_Skill(Applicant, Skill):
    pass

class Applicant_Position(Applicant, Position):
    pass
