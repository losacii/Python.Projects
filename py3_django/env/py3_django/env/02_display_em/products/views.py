from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)

def about(request):
    return HttpResponse('about page')