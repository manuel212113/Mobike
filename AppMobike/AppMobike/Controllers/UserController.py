from django.shortcuts import render,redirect,HttpResponse

import pyrebase


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


def Dashboard(request):
    correo=request.POST.get('email')
    contraseña=request.POST.get('pass')
    
    return render(request,'views/Dashboard.html', {"em":correo} )





    

