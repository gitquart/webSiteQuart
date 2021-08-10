from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


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
        response=None

        #Database logic here...

        return JsonResponse({'logged':response}, status=200)




