from django.shortcuts import render,redirect,HttpResponse

import pyrebase

from AppMobike.models import UserMobike


from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model





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


#contador
counter=0



def GetCurrentUser(request):
    current_user=request.user.username
    return current_user
 


def DashboardUser(request):
    current_user = request.user.username
    rol=''
    if UserMobike.objects.filter(username=current_user, user_type='Funcionario'):
        rol='Funcionario'
        return render(request,'views/Dashboard.html' ,{'username':current_user, 'rol_user':rol } )

    elif UserMobike.objects.filter(username=current_user, user_type='Administrador'):
        rol='Administrador'
        return render(request,'views/Dashboard.html' ,{'username':current_user, 'rol_user':rol} )


    else:
      return redirect("http://127.0.0.1:8000/")


def DisplayUserList(request):
     all_users={}
     all_users = UserMobike.objects.values()
     current_user=GetCurrentUser(request)
     all_users = list(all_users)
     return render(request,'views/users.html', {'ListUsers':all_users, 'username':current_user})






    

