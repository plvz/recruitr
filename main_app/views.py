# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Position
from .forms import PositionForm
# Create your views here.
# Create your views here.
def index(request):
    return render(request,'index.html')

def positions(request):
    positions = Position.objects.all()
    form = PositionForm()
    return render(request,'positions.html',{'positions':positions, 'form':form})

def post_position(request):
    form = PositionForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')
