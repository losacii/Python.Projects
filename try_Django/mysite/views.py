# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

def home(request):
    if True: # change it to some EVENTS later...
        messages.success(request, 'Account created for !')
    template = "home.html"
    context = {"userName": 'losacii'}
    return render(request, template, context)

def about(request):
    template = "about.html"
    context = {"company": 'X company'}
    return render(request, template, context)