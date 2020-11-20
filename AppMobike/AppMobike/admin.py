from django.contrib import admin

from .models import UserMobike
from .models import BikeStations
from .models import BikesModel


admin.site.register(UserMobike)
admin.site.register(BikeStations)
admin.site.register(BikesModel)


