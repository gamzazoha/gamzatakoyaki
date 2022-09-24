from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('food/', views.food),
    path('beauty/', views.beauty),
    path('place/', views.place),
    path('place/place1/', views.place1),
    path('food/food1/', views.food1),
    path('food/food1/reservation_pos/', views.reservation_pos),
    path('place/place1/reservation_imp/', views.reservation_imp),
]