from django.contrib import admin
from django.urls import path
from . import views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home, name='home'),
    path('about/', homeViews.about, name='about'),
]
