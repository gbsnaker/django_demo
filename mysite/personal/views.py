# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'personal/home.html')

def content(request):
    names = ["gbsnaker","king","gb" ] 
    return render(request, 'personal/content.html',{'names': names})