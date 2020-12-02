from django.contrib import admin

from .models import UserMobike
from .models import BikeStations
from .models import BikesModel
from .models import BicycleParking
from .models import CC_INFO
from .models import BicycleTravel
from .models import TransactionsModel


admin.site.register(UserMobike)
admin.site.register(BikeStations)
admin.site.register(BikesModel)
admin.site.register(BicycleParking)
admin.site.register(CC_INFO)
admin.site.register(BicycleTravel)
admin.site.register(TransactionsModel)




