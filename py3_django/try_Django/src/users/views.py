# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, now you can log in!')
            return redirect('user-login')
    else:
        form = UserRegisterForm()

    template = "users/register.html"
    context = {"form": form}
    return render(request, template, context)

@login_required
def profile(request):
    template = 'users/profile.html'
    return render(request, template)