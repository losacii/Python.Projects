from django.contrib import admin
from django.urls import path, include
from . import views as homeViews
import blog.views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home, name='home'),
    path('about/', homeViews.about, name='about'),

    path('blog/', blogViews.blogHome, name='blog-home'),
]
