# views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    template = "home.html"
    context = {"userName": 'losacii'}
    return render(request, template, context)

def about(request):
    template = "about.html"
    context = {"company": 'X company'}
    return render(request, template, context)