# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    def __unicode__(self):
        return self.skill

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    number_position = models.DecimalField(max_digits=5, decimal_places=0)
    description = models.TextField()
    position_skills = models.ManyToManyField(Skill)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    '''phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
                                '''
    seniority = models.DecimalField(max_digits=3, decimal_places=0)
    employee_skills = models.ManyToManyField(Skill)

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    angel_url = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    apllicant_skills = models.ManyToManyField(Skill)
    applicant_positions = models.ManyToManyField(Position)
