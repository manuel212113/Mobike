from django.contrib.auth.decorators import login_required
from AppMobike.models import UserMobike
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
import pyrebase

from AppMobike.models import BikeStations
from AppMobike.models import BikesInfo
from AppMobike.models import BicycleParking
from AppMobike.models import BicycleTravel

from AppMobike.Controllers import UserController
from AppMobike.models import TransactionsModel

from django.core import serializers

from django.core.serializers.json import DjangoJSONEncoder

@login_required
def RentBike(request):

  
    if UserController.CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )

    profileImage=(UserController.GetProfileImage(request))

    BikeStations_all = BikeStations.objects.values_list()
    travel_success=False

    json_serializer = serializers.get_serializer("json")()
    stations = json_serializer.serialize(BikeStations.objects.all().order_by('name'), ensure_ascii=False)
    current_username=UserController.GetCurrentUser(request)
    current_id_user=UserController.GetCurrentUserId(request)

    BikeStations_list={}
    BikeStations_list = BikeStations.objects.values('name','Longitude','Latitude')
    Bikes=json_serializer.serialize(BikesInfo.objects.all().order_by('code_bike'), ensure_ascii=False)
    BicyclePark=json_serializer.serialize(BicycleParking.objects.all().order_by('name'), ensure_ascii=False)



    
    return render(request,'views/rentbike.html',{'username':current_username,'user_id':current_id_user,'profileImage':profileImage,'BikeStations':stations,'listStations':BikeStations_list,'Bikes':Bikes,'Park':BicyclePark})




@login_required
def AddTravel(request,id,destination,InitialStation,FinalStation,value):
       if UserController.CheckStatusAccount(request):
          return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )
       
       BikeStations_all = BikeStations.objects.values_list()
       travel_success=True
       json_serializer = serializers.get_serializer("json")()
       stations = json_serializer.serialize(BikeStations.objects.all().order_by('name'), ensure_ascii=False)
       BikeStations_list={}
       BikeStations_list = BikeStations.objects.values('name','Longitude','Latitude')
       Bikes=json_serializer.serialize(BikesModel.objects.all().order_by('code_bike'), ensure_ascii=False)
       BicyclePark=json_serializer.serialize(BicycleParking.objects.all().order_by('name'), ensure_ascii=False)
       profileImage=(UserController.GetProfileImage(request))
       current_username=UserController.GetCurrentUser(request)
       bt = BicycleTravel(Destination=destination, Location=InitialStation,InitialStation=InitialStation,FinalStation=FinalStation,user=current_username)
       bt.save()
       Transaction=TransactionsModel(user=current_username,value_travel=value)
       Transaction.save()
       return redirect('/Dashboard/rent')

 


      

