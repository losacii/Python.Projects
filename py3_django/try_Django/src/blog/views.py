# blog/views.py
from django.shortcuts import render
from .models import Post

def blogHome(request):
    template = "blogHome.html"
    context = {"posts": Post.objects.all()}
    return render(request, template, context)
