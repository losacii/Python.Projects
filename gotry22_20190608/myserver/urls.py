# urls.py

from django.contrib import admin
from django.urls import path, include
from . import views as homeViews
import blog.views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home, name='main-home'),          # home
    path('about/', homeViews.about, name='main-about'),
    path('blog/', include('blog.urls')), # blog
    path('blog-new/', blogViews.post_create_view , name='blog-new'),
    path('contact/', homeViews.contact_1, name='main-contact'),
]
