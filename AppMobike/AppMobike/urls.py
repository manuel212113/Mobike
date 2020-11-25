"""AppMobike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

import include
from django.contrib import admin

from AppMobike.Controllers import HomeController
from AppMobike.Controllers import UserController
from AppMobike.Controllers import ClienteController

from django.conf import settings

from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),

    path('',LoginView.as_view(template_name='views/index.html') , name='login'),
    path('register',UserController.Register,name='Register'),
    path('Facebook', HomeController.FacebookPage, name='FacebookPage'),
    path('Dashboard',login_required(UserController.DashboardUser), name='DashboardUser'),
    path('logout', LogoutView.as_view(template_name='views/index.html'), name='logout'),
    path('Dashboard/users', UserController.DisplayUserList, name='DisplayUserList' ),
    path('Dashboard/users/delete/<int:id>', login_required(UserController.DeleteUser), name='DeleteUser'),
    path('Dashboard/users/block/<int:id>', login_required(UserController.BlockUser), name='BlockUser'),
    path('Dashboard/users/update/<int:id>/<str:user_type>', login_required(UserController.UpdateUserType), name='UpdateUserType'),
    path('Dashboard/rent', ClienteController.RentBike, name='RentBike' ),


    



]  + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




