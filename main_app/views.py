# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from os import environ
from datetime import timedelta
import datetime
import pytz

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery
from oauth2client import client,tools
from oauth2client.file import Storage

from django.core.mail import send_mail,get_connection
from django.core import mail
from django.core.mail.message import EmailMessage
import re

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Position, Skill, Applicant, Employee
from .forms import PositionForm, ApplicantForm, EmployeeForm, EventForm

# Google calendar code
service_account_email = os.getenv("SERVICE_ACCOUNT_EMAIL")

CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")
APPLICATION_NAME = 'Recruitr Calendar API Python DJANGO'

SCOPES = 'https://www.googleapis.com/auth/calendar'
scopes = [SCOPES]
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

my_host = os.getenv("HOST")
my_port = 587
my_password = os.getenv('PASSWORD')
print(my_password)
my_use_tls = True
connection = get_connection(host=my_host,
                            port=my_port,
                            username=service_account_email,
                            password=my_password,
                            use_tls=my_use_tls)

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials



def post_event(request):
    form = EventForm(request.POST)


    print(form.__dict__)
    if form.is_valid():
        event = form.save(commit = False)

        credentials =  get_credentials()
        http = credentials.authorize(httplib2.Http())

        service = build('calendar', 'v3', http=http)
        #create_event()
        start_datetime = datetime.datetime.now(tz=pytz.utc)
        start_datetime = start_datetime.replace(year=event.date.year)
        start_datetime = start_datetime.replace(month=event.date.month)
        start_datetime = start_datetime.replace(day=event.date.day)
        start_datetime = start_datetime.replace(hour=event.schedule.hour)
        start_datetime = start_datetime.replace(minute=event.schedule.minute)
        print(event.duration)
        print(start_datetime)

        send_mail(
        'Interview',
        'Hello, your are invited for an Interview the'+str(start_datetime),
        'gpellevoizin37@gmail.com',
        [event.target_email,event.target_email],
        fail_silently=False,
        connection=connection,
        )
        employee_email = event.target_email
        candidate_email = event.target_email1
        duration=event.duration
        start_datetime = start_datetime.replace(hour=event.schedule.hour-1)
        gmailpattern = re.compile("^.*@gmail.com$")

        if gmailpattern.match(event.target_email):
            event = service.events().insert(calendarId=employee_email, body={
            'summary': 'Recruitr Interrview',
            'description': 'Interview with one of our applicant',
            'start': {'dateTime': start_datetime.isoformat()},
            'end': {'dateTime': (start_datetime + timedelta(minutes=int(duration))).isoformat()},
            }).execute()

        if gmailpattern.match(candidate_email) :
            event = service.events().insert(calendarId=candidate_email, body={
            'summary': 'Recruitr Interrview',
            'description': 'Interview with one of our staff',
            'start': {'dateTime': start_datetime.isoformat()},
            'end': {'dateTime': (start_datetime + timedelta(minutes=int(duration))).isoformat()},
            }).execute()
    else:
        print('form is invalid')
    return HttpResponseRedirect('/')




# Views here.
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
    connection = mail.get_connection()
    # Manually open the connection
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
    skills = [None]*100
    c=0
    eventform = EventForm()
    for c in range(0,length):
        skills[c] = position.position_skills.all()[c].skill_id
    employees = Employee.objects.filter(employee_skills__in=skills).order_by('-seniority')[:10]
    return render(request, 'applicant.html',{'applicant':applicant,'position':position,'employees':employees,'eventform':eventform})

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
