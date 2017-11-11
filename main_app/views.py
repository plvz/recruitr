# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Position, Skill, Applicant, Employee
from .forms import PositionForm, ApplicantForm, EmployeeForm
# Create your views here.
# Create your views here.
def index(request):
    return render(request,'index.html')

def positions(request):
    positions = Position.objects.all()
    skills = Skill.objects.all()
    form = PositionForm()
    return render(request,'positions.html',{'positions':positions, 'form':form,'skills':skills})

def post_position(request):
    form = PositionForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    else:
        print('form is invalid')
    return HttpResponseRedirect('/')

def detail_position(request,position_id):
    position = Position.objects.get(position_id=position_id)
    applicants = Applicant.objects.filter(applicant_positions=1)
    applicantform = ApplicantForm()
    return render(request, 'detail.html', {'position':position,'applicantform':applicantform,'applicants':applicants})

def post_applicant(request,position_id):
    position = Position.objects.get(position_id=position_id)
    form = ApplicantForm(request.POST)
    if form.is_valid():
        user = form.save(commit = True)
        user.applicant_positions.add(position)
        print(user.__dict__)
    else:
        print('form is invalid')
    return HttpResponseRedirect('/'+str(position_id)+'/applicant/'+str(user.id))

def detail_applicant(request,position_id,applicant_id):
    applicant = Applicant.objects.get(id=applicant_id)
    position = Position.objects.get(position_id=position_id)
    length = len(position.position_skills.all())
    skills = [None]
    c=0
    for c in range(0,length):
        skills[c] = position.position_skills.all()[c].skill_id
    employees = Employee.objects.filter(employee_skills__in=skills).order_by('-seniority')[:10]
    return render(request, 'applicant.html',{'applicant':applicant,'position':position,'employees':employees})

def employee(request):
    employeeform = EmployeeForm()
    return render(request, 'employee.html',{'employeeform':employeeform})

def post_employee(request):
    form = EmployeeForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    else:
        print('form is invalid')
    return HttpResponseRedirect('/')
