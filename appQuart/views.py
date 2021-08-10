from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import postgresql as db


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
        strusername=str(request.POST['username'])
        strpwd=str(request.POST['pwd'])

        #Check if user is in database
        res=None
        print('-------------1-----------------')
        response=False
        print('-------------2-----------------')
        query=f"select id from usuario where correo='{strusername}' and contrasena='{strpwd}' "
        print(query)
        print('-------------3-----------------')
        res=db.getQuery(query)
        print('-------------4-----------------')
        if res: 
            #User already registered 
            response=True

        return JsonResponse({'logged':response}, status=200)




