from django.contrib import admin
from django.urls import path, include
from . import views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home),
    path('p5js_page/', homeViews.p5js_page),
    path('p5js_page/<str:sname>/', homeViews.p5js_page_show)
]
