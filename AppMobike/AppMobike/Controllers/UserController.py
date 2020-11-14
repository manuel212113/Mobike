from django.shortcuts import render,get_object_or_404,redirect,HttpResponse

import pyrebase

from AppMobike.models import UserMobike


from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model


from django.contrib.auth.decorators import login_required





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




def CheckStatusAccount(request):
     status_account = UserMobike.objects.get(id=request.user.id)

     if status_account.state_account == False:
        return True

def GetCurrentUser(request):
    current_user=request.user.username
    return current_user
 


def DashboardUser(request):
    current_user = request.user.username
    
    if CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )



 
    rol=''
    if UserMobike.objects.filter(username=current_user, user_type='Funcionario'):
        rol='Funcionario'
        return render(request,'views/Dashboard.html' ,{'username':current_user, 'rol_user':rol } )

    elif UserMobike.objects.filter(username=current_user, user_type='Administrador'):
        rol='Administrador'
        return render(request,'views/Dashboard.html' ,{'username':current_user, 'rol_user':rol} )


    else:
      return redirect("http://127.0.0.1:8000/")

@login_required
def DisplayUserList(request):

     if CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )


     all_users={}
     all_users = UserMobike.objects.values()
     current_user=GetCurrentUser(request)
     all_users = list(all_users)
     return render(request,'views/users.html', {'ListUsers':all_users, 'username':current_user})


@login_required
def DeleteUser(request,id):
   
    if CheckStatusAccount(request)==False:
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )


    obj= get_object_or_404(UserMobike,id=id)
    obj.delete()


    return redirect('/Dashboard/users') 


@login_required
def BlockUser(request,id):
   
   if CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )
   
   
   status_account = UserMobike.objects.get(id=id)

   
   if status_account.state_account == False:
       print('Actualizar en false')
       UserMobike.objects.filter(id=id).update(state_account=True)
       return redirect('/Dashboard/users')
   elif status_account.state_account == True:
       print('Actualizar en True')
       UserMobike.objects.filter(id=id).update(state_account=False)
       return redirect('/Dashboard/users')



     


    

