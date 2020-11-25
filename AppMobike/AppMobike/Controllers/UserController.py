from django.shortcuts import render,get_object_or_404,redirect,HttpResponse

import pyrebase

from AppMobike.models import UserMobike

from AppMobike.models import CreditCardInfo


from AppMobike.forms import UserForm


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

def GetProfileImage(request):
    ProfileImage=request.user.Image_Profile
    return ProfileImage


def GetCurrentUser(request):
    current_user=request.user.username
    return current_user
 

def GetEmailCurrentUser(request):
    email=request.user.email
    return email

def GetCurrentTypeUser(request):
    user_type=request.user.user_type
    return user_type



def ShowRegisterForm(request):
    return render(request,'views/register.html')



def Register(request):
	if request.user.is_authenticated:
		return redirect('http://127.0.0.1:8000')
	else:
		form = UserForm()
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Cuenta Creada del usuario:  ' + user)

				return redirect('http://127.0.0.1:8000/Dashboard')
			

		context = {'form':form}
		return render(request, 'views/register.html', context)




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

    elif UserMobike.objects.filter(username=current_user, user_type='Cliente'):
        rol='Cliente'
        return render(request,'views/Dashboard.html' ,{'username':current_user, 'rol_user':rol} )


    else:
      return redirect("http://127.0.0.1:8000/")

@login_required
def DisplayUserList(request):

     if CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )

     if GetCurrentTypeUser(request)=="Funcionario" or GetCurrentTypeUser(request)=="Cliente":
        return HttpResponse("<h1>Acceso Denegado </h1> <a href=/Dashboard>ir Al Panel de Inicio</a> ." )


     all_users={}
     all_users = UserMobike.objects.values()
     current_user=GetCurrentUser(request)
     all_users = list(all_users)
     return render(request,'views/users.html', {'ListUsers':all_users, 'username':current_user})


@login_required
def DeleteUser(request,id):

    if GetCurrentTypeUser(request)=="Funcionario" or GetCurrentTypeUser(request)=="Cliente":
        return HttpResponse("<h1>Acceso Denegado </h1> <a href=/Dashboard>ir Al Panel de Inicio</a> ." )
   
    if CheckStatusAccount(request)==False:
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )


    obj= get_object_or_404(UserMobike,id=id)
    obj.delete()


    return redirect('/Dashboard/users') 


@login_required
def BlockUser(request,id):
   
   if CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )
   

   if GetCurrentTypeUser(request)=="Funcionario" or GetCurrentTypeUser(request)=="Cliente":
        return HttpResponse("<h1>Acceso Denegado </h1> <a href=/Dashboard>ir Al Panel de Inicio</a> ." )

   status_account = UserMobike.objects.get(id=id)

   
   if status_account.state_account == False:
       UserMobike.objects.filter(id=id).update(state_account=True)
       return redirect('/Dashboard/users')
   elif status_account.state_account:
       UserMobike.objects.filter(id=id).update(state_account=False)
       return redirect('/Dashboard/users')




def UpdateUserType(request,id,user_type):

    if CheckStatusAccount(request):
        return HttpResponse("<h1>Tu Cuenta esta Bloqueda Contacta con Administración </h1> <a href=/logout>Cerrar Sesion</a> ." )
   

    if GetCurrentTypeUser(request)=="Funcionario" or GetCurrentTypeUser(request)=="Cliente":
        return HttpResponse("<h1>Acceso Denegado </h1> <a href=/Dashboard>ir Al Panel de Inicio</a> ." )
    UserMobike.objects.filter(id=id).update(user_type=user_type)
    return redirect('/Dashboard/users')



     


    

