from django.contrib import admin
from django.urls import path,include
from AppMobike.Controllers import HomeController 
from AppMobike.Controllers import UserController 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
import include


urlpatterns = [
    
     path('', include('AppMobike.urls')),
  
    

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
