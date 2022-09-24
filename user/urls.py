from django.urls import path
from . import views  
 
urlpatterns = [
   path('register/',views.register),
   path('login/', views.login  ),
   path('logout/', views.logout  ), 
   #즉, 최종적인 url은 127~~~~:8000/user/register가 된다.
] 