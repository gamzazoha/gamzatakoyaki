from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('food/', views.food),
    path('beauty/', views.beauty),
    path('place/', views.place),
]