from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('login_owner/', views.login, name='login_owner'),
    path('logout/', views.logout, name='logout'),
] 