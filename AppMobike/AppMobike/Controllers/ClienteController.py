from django.contrib.auth.decorators import login_required
from AppMobike.models import UserMobike
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
import pyrebase

from AppMobike.models import BikeStations
from AppMobike.models import BikesModel

from AppMobike.Controllers import UserController

from django.core import serializers

from django.core.serializers.json import DjangoJSONEncoder

def RentBike(request):

    profileImage=(UserController.GetProfileImage(request))

    BikeStations_all = BikeStations.objects.values_list()
    
    json_serializer = serializers.get_serializer("json")()
    stations = json_serializer.serialize(BikeStations.objects.all().order_by('name'), ensure_ascii=False)
    current_user=UserController.GetCurrentUser(request)

    BikeStations_list={}
    BikeStations_list = BikeStations.objects.values('name','Longitude','Latitude')
    Bikes=json_serializer.serialize(BikesModel.objects.all().order_by('code_bike'), ensure_ascii=False)


    
    return render(request,'views/rentbike.html',{'username':current_user,'profileImage':profileImage,'BikeStations':stations,'listStations':BikeStations_list,'Bikes':Bikes})