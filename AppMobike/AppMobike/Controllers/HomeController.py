from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView


def HomePage(request):
    
    return render(request,LoginView.as_view(template_name='views/index.html'))




def FacebookPage(request):
    return redirect("https://www.facebook.com/MobikeCL/")

      
