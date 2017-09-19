# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import render_to_response


# Create your views here.
def index2(request):     #This is the index page (main page) for testApp
    return HttpResponse("Hei. Dette er en testside")

def index3(request):
    template = loader.get_template("testApp/index.html")
    return HttpResponse(template.render(request))

def index4(request):
    return render_to_response('testApp/index.html')

def index5(request):
    # View code here...
    return render(request, 'testApp/index.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')

def index(request):
    return render(request, 'testApp/index.html')

def hei(request):
	return HttpResponse("HEISANN!")

def brann(request):
	return HttpResponse("""<p style="color:red;"> BRANN!! </p>""")
