from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserMobikeManager(BaseUserManager):
    def create_user(self,email,username,name,last_name,password = None):
        if not email:
            raise ValueError('El Usuario debe tener un correo Electronico')

        user=self.model(
         username=username,
         email=self.normalize_email(email), 
         name=name,
         last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,name,last_name,password):
        
        user=self.create_user(
         email , 
         username=username,
         name=name, 
         last_name=last_name,
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
     Image_Profile = models.ImageField('Imagen de Perfil', upload_to='profile/',  height_field=None, width_field=None, max_length=200)
     state_account = models.BooleanField( default=True)
     admin_user = models.BooleanField( default=False)
     objects=UserMobikeManager() 
     
     USERNAME_FIELD= 'username'

     REQUIRED_FIELDS=['email','name','last_name']

     def __str__(self):
         return f'{self.name},{self.last_name}'
     def has_perm(self,obj=None):
         return True

     def has_module_perms(self,app_label):
         return True 

     @property
     def is_staff(self):
         return self.admin_user 
