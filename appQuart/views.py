from django.shortcuts import render
from django.http import JsonResponse
from appQuart.models import Usuario
from django.db import connection


"""
"render" automatically looks for the views in "templates" folder of each app, i.e. "appQuart/templates"
"""
# Create your views here.

def index(request):
    return render(request,'index.html')

def tradingNewsApp_login(request):
    return render(request,'trading_app_login.html')

def tradingNewsApp_register(request):
    return render(request,'trading_app_register.html')

#tradingNewsApp
#Once the user is logged, he/she will be redirected to the main trading_app.html
def tradingNewsApp(request):
    return render(request,'trading_app.html')

def login(request):
    #In trading_app_login.html javascript already has a filter for empty values
    #request.is_ajax() is TRUE 
    if request.is_ajax() and request.method == "POST":
        #Close active connections if any
        connection.close()
        strmail=str(request.POST['mail'])
        strpwd=str(request.POST['pwd'])
        response=0
        #Database logic here...
        #Look for the mail, if it already exists: Login, if not then Register
        resultQuery=None
        try:
            resultQuery=Usuario.objects.filter(correo=strmail,contrasena=strpwd)
        except:
            response=0
            resultQuery=None    

        #Seems that fetching the total of rows from resultQuery makes trouble on connection,
        #checking resultQuery is enough
        if resultQuery:
            response=1
        else:
            response=0    

        
        
        return JsonResponse({'logged':response}, status=200)




