from django.shortcuts import render,redirect


import pyrebase

from django.contrib.auth.models import User


#Firebase Configuracion
config = {
      "apiKey": "AIzaSyB_nM8zuy5DfozLocoqtYW9t0mJTn7eCTQ",
      "authDomain": "mobike-8943a.firebaseapp.com",
      "databaseURL": "https://mobike-8943a.firebaseio.com",
      "projectId": "mobike-8943a",
      "storageBucket": "mobike-8943a.appspot.com"
       }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()





def HomePage(request):
    return render(request,'views/index.html')




def FacebookPage(request):
    return redirect("https://www.facebook.com/MobikeCL/")


def Dashboard(request):
    current_user = request.user
    if User.objects.filter(username=current_user, groups__name='Funcionario').exists():
        return render(request,'views/index2.html' ,{'username':current_user} )
    else:
      return redirect("http://127.0.0.1:8000/")

  


