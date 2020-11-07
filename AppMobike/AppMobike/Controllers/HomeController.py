from django.shortcuts import render,redirect


def HomePage(request):
    return render(request,'views/index.html')




def FacebookPage(request):
    return redirect("https://www.facebook.com/MobikeCL/")

      
