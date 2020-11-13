from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView


    




def FacebookPage(request):
    return redirect("https://www.facebook.com/MobikeCL/")


def HomePage(request):
    return redirect("http://127.0.0.1:8000/")

      
