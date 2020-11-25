from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserMobikeManager(BaseUserManager):
    def create_user(self,email,username,name,last_name,RUT,password = None):
        if not email:
            raise ValueError('El Usuario debe tener un correo Electronico')

        user=self.model(
         username=username,
         email=self.normalize_email(email), 
         name=name,
         RUT=RUT,
         last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,name,last_name,RUT,password):
        
        user=self.create_user(
         email , 
         username=username,
         name=name, 
         last_name=last_name,
         RUT=RUT,
         password=password

        )
        user.admin_user=True
        user.user_type='Administrador'
        user.save()
        return user
       

class UserMobike(AbstractBaseUser):
     username=models.CharField('Nombre de usuario', unique=True,max_length=100)
     email=models.EmailField('Correo Electronico',max_length=254,unique=True)
     name=models.CharField('Nombre',max_length=200,blank=False,null=False)
     last_name=models.CharField('Apellido',max_length=200)
     user_type=models.CharField( max_length=300, default='Cliente')
     account_balance=models.CharField(max_length=50,default="0")
     Image_Profile = models.ImageField('Imagen de Perfil',   height_field=None, width_field=None, max_length=200)
     state_account = models.BooleanField( default=True)
     RUT=models.CharField('RUT',max_length=13 , unique=True)
     admin_user = models.BooleanField( default=False)
     objects=UserMobikeManager() 
     
     USERNAME_FIELD= 'username'

     REQUIRED_FIELDS=['email','name','last_name','RUT']

     class Meta:
          verbose_name_plural="RUT"
     def __str__(self):
          return self.RUT
     def has_perm(self,obj=None):
         return True

     def has_module_perms(self,app_label):
         return True 

     @property
     def is_staff(self):
         return self.admin_user 



class BikeStations(models.Model):
      name= models.CharField('Nombre Estacion', max_length=200,unique=True,null=False) 
      Latitude= models.DecimalField('Latitud',max_digits=22, decimal_places=8, blank=True, null=False)
      Longitude= models.DecimalField('Longitud',max_digits=22, decimal_places=9, blank=True, null=False)

      class Meta:
          verbose_name_plural="Estacion"
      def __str__(self):
          return self.name


class BikesModel(models.Model):
      MODELS_BIKE=(('cannondale habit 1','CANNONDALE HABIT 1'),('canyon lux cf slx 9.0','CANYON LUX  9.0'),('cube ams 100','CUBE AMS 100'))
      code_bike=models.CharField('Numero Bicicleta',max_length=15,null=False,unique=True)
      bike_model=models.CharField('Modelo Bicicleta', max_length=50,choices=MODELS_BIKE )
      state_bike=models.CharField('Estado Bicicleta', max_length=30, default="Libre")
      ## Estacion de la bicicleta ##
      station=models.ForeignKey(BikeStations,verbose_name="Estacion",default=000, on_delete=models.SET_DEFAULT)


class CreditCardInfo(models.Model):
      CreditCardNumber=models.IntegerField('Numero Tarjeta de Credito',max_length=16, null=False, unique=True)
      CV=models.IntegerField('Codigo Seguridad Tarjeta de Credito',max_length=3, null=False, unique=True)
      MONTH=models.IntegerField('Mes Vencimiento',max_length=2, null=False)
      YEAR=models.IntegerField('Año Vencimiento',max_length=4, null=False)
      OWNER=models.ForeignKey(UserMobike,verbose_name="RUT",default=000, on_delete=models.SET_DEFAULT)


      




