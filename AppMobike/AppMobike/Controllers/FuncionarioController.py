from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from AppMobike.models import TransactionsModel
from AppMobike.models import BicycleTravel
from AppMobike.Controllers import UserController
from AppMobike.models import UserMobike
import datetime
import random
from datetime import date
from api2pdf import Api2Pdf
import pdfkit
from django.db.models import Count





@login_required
def Transactions(request):




    all_Transactions={}
    all_Transactions = TransactionsModel.objects.values()
    current_user=UserController.GetCurrentUser(request)
    all_Transactions = list(all_Transactions)
    return render(request,'views/Transactions.html', {'allTransactions':all_Transactions, 'username':current_user})




@login_required

def frequentArea(request):




    all_frequentArea={}
    all_frequentArea = BicycleTravel.objects.values()
    current_user=UserController.GetCurrentUser(request)
    all_frequentArea = list(all_frequentArea)
    return render(request,'views/frequentArea.html', {'all_frequentArea':all_frequentArea, 'username':current_user})




def ViewPDFTransactions(request,id,doc):
   
    if UserMobike.objects.filter(id=id, user_type='Cliente'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    elif UserMobike.objects.filter(id=id, user_type='Administrador'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    

    all_Transactions={}
    all_Transactions = TransactionsModel.objects.values()
    current_user=request.user.username
    all_Transactions = list(all_Transactions)
    date = datetime.datetime.now()
    number_doc=random.randint(1,800)
    today = date.today()
    date=today.strftime("%d/%m/%Y")


    return render(request, 'views/reportTransaction.html',{'allTransactions':all_Transactions, 'username':current_user,'date':date,'doc_num':number_doc})




def ViewPDFFrequentArea(request,id,doc):
    
    if UserMobike.objects.filter(id=id, user_type='Cliente'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    elif UserMobike.objects.filter(id=id, user_type='Administrador'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    

    all_FrequentArea={}
    all_FrequentArea = BicycleTravel.objects.values().order_by().annotate(Count('InitialStation'))
    current_user=request.user.username
    all_FrequentArea = list(all_FrequentArea)
    date = datetime.datetime.now()
    number_doc=random.randint(1,800)
    today = date.today()
    date=today.strftime("%d/%m/%Y")


    return render(request, 'views/reportFrequentArea.html',{'allFrequentArea':all_FrequentArea, 'username':current_user,'date':date,'doc_num':number_doc})



@login_required
def GeneratePdfFrequentArea(request):
    current_user=request.user.id	

    if UserMobike.objects.filter(id=current_user, user_type='Cliente'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    elif UserMobike.objects.filter(id=current_user, user_type='Administrador'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    options = {
    'quiet': ''
    }
    number_doc=random.randint(1,800)
    number_doc=str(number_doc)
    current_user=str(current_user)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    url='http://127.0.0.1:8000/Dashboard/reports/frequentArea/pdf/'+current_user+'/'+number_doc

    pdf = pdfkit.from_url(url,False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="doc_Zona_Frecuente-'+number_doc+'.pdf"'

    return response


@login_required    
def GeneratePdfTransactions(request):
    current_user=request.user.id	
    if UserMobike.objects.filter(id=current_user, user_type='Cliente'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    elif UserMobike.objects.filter(id=current_user, user_type='Administrador'):
        return HttpResponse('<h1>Acceso Denegado</h1>')
    
    options = {
    'quiet': ''
    }
    number_doc=random.randint(1,800)
    number_doc=str(number_doc)
    current_user=str(current_user)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    url='http://127.0.0.1:8000/Dashboard/reports/transactions/pdf/'+current_user+'/'+number_doc

    pdf = pdfkit.from_url(url,False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="doc_transacciones-'+number_doc+'.pdf"'

    return response




  




