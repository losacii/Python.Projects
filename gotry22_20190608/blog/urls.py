# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='blog-list'),
    path('<str:slug>/', views.post_detail_view), 
    path('<str:slug>/edit/', views.post_update_view), 
    path('<str:slug>/delete/', views.post_delete_view), 
    path('<str:slug>/update/', views.post_update_view), 
]