# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):     #This is the index page (main page) for testApp
    return HttpResponse("Hei. Dette er en testside")
