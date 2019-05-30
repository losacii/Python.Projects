from django.contrib import admin
from django.urls import path, include
from . import views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home)
]
