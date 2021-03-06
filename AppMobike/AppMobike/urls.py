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

from django.contrib import admin
from django.conf.urls import include

from AppMobike.Controllers import HomeController
from AppMobike.Controllers import UserController
from AppMobike.Controllers import ClienteController
from AppMobike.Controllers import FuncionarioController

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
    path('Dashboard/rent/add/<int:id>/<str:destination>/<str:InitialStation>/<str:FinalStation>/<str:value>', ClienteController.AddTravel, name='AddTravel' ),
    path('Dashboard/reports/transactions',FuncionarioController.Transactions,name='Transactions'),
    path('Dashboard/reports/frequentArea',FuncionarioController.frequentArea,name='frequentArea'),
    path('Dashboard/reports/transactions/pdf/<str:id>/<str:doc>',FuncionarioController.ViewPDFTransactions,name='ViewPDFTransactions'),
    path('Dashboard/reports/transactions/create/pdf', FuncionarioController.GeneratePdfTransactions , name='GeneratePdfTransactions'),
    path('Dashboard/reports/frequentArea/pdf/<str:id>/<str:doc>',FuncionarioController.ViewPDFFrequentArea,name='ViewPDFFrequentArea'),
    path('Dashboard/reports/frequentArea/create/pdf', FuncionarioController.GeneratePdfFrequentArea , name='GeneratePdfFrequentArea'),
    path('Dashboard/park/add', UserController.AddParkStation , name='AddParkStation'),
    path('Dashboard/park/add/new/<str:lat>/<str:lon>/<str:name>', UserController.AddNewParkStation , name='AddNewParkStation'),
    path('Dashboard/park/list', UserController.ListParkStation , name='ListParkStation'),
    path('Dashboard/bike/add', UserController.AddBike , name='AddBike'),
    path('Dashboard/bike/add/new/<str:cod_bici>/<str:modelo_bici>/<str:estacion_bici>', UserController.AddNewBike , name='AddNewBike'),
    path('Dashboard/bike/list', UserController.ListBike , name='ListBike'),
    path('Dashboard/station/add', UserController.AddStation, name='AddStation'),
    path('Dashboard/station/list', UserController.ListStation, name='ListStation'),
    path('Dashboard/station/add/new/<str:lat>/<str:lon>/<str:name>', UserController.AddNewStation,name='AddNewStation')





    



]  + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




