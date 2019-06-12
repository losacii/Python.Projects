from django.shortcuts import render
import os
from . import settings

def home(request):
    scriptDir = os.path.join(settings.BASE_DIR, 'templates', 'p5js', 'scripts')
    names = os.listdir(scriptDir)
    names.sort()
    context = {"p5scripts": names }
    template = 'home/home.html'
    return render(request, template, context)

def p5js_page(request):
    template = 'p5js/home.html'
    return render(request, template)

def p5js_page_show(request, sname):
    context = { "url": f"p5js/scripts/{sname}" }
    template = 'p5js/home.html'
    return render(request, template, context)