from django import forms

from .models import UserMobike
from .models import CC_INFO


from django.contrib.auth.forms import UserCreationForm




class UserForm(UserCreationForm):
     class Meta:
       model = UserMobike
       fields = ['name', 'last_name', 'RUT', 'email','username','password1','password2','Image_Profile']






