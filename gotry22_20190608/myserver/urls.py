# urls.py

from django.contrib import admin
from django.urls import path, include
from . import views as homeViews
import blog.views as blogViews
from django.conf import settings
from searches.views import search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home, name='main-home'),          # home
    path('about/', homeViews.about, name='main-about'),
    path('blog/', include('blog.urls')), # blog
    path('blog-new/', blogViews.post_create_view , name='blog-new'),
    path('contact/', homeViews.contact_1, name='main-contact'),
    path('search/', search_view),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
