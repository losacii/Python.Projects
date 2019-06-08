# views.py

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home(request):
    context = {"title": 'home-page'}
    template = 'home/home.html'
    return render(request, template, context)

def about(request):
    template = 'home/about.html'
    return render(request, template)

def contact_0(request):
    print(request.POST)
    context = {"title": 'Contact Us'}
    template = 'home/form.html'
    return render(request, template, context)

def contact_1(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print("----------->\n", form.cleaned_data)
    else:
        print("---------- not valid form")

    context = {"title": 'Contact Us', "form": form }
    template = 'home/form.html'
    return render(request, template, context)