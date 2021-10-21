from django.shortcuts import render
from django.http import JsonResponse
from appQuart.models import Usuario


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

def login(request):
    #In trading_app_login.html javascript already has a filter for empty values
    if request.is_ajax and request.method == "POST":
        strmail=str(request.POST['mail'])
        strpwd=str(request.POST['pwd'])
        response=0
        #Database logic here...
        #Look for the mail, if it already exists: Login, if not then Register
        resultQuery=None
        resultQuery=Usuario.objects.filter(correo=strmail,contrasena=strpwd)
        if resultQuery.count()>0:
            response=1
        
        return JsonResponse({'logged':response}, status=200)




