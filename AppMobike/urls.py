from django.contrib import admin
from django.urls import path,include
from AppMobike.Controllers import HomeController 
from AppMobike.Controllers import UserController 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
     path('', include('AppMobike.urls')),
  
    

]
 