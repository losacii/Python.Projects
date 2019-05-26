from django.contrib import admin
from django.contrib.auth import views as authViews
from django.urls import path, include

from . import views as homeViews
import blog.views as blogViews
import users.views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home, name='home'),
    path('about/', homeViews.about, name='about'),

    path('blog/', blogViews.blogHome, name='blog-home'),

    path('register/', userViews.register, name='user-register'),
    path('profile/', userViews.profile, name='user-profile'),

    path('login/',  authViews.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),

]
