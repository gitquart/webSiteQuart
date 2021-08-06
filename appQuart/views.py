from django.shortcuts import render
from django.http import HttpResponse

"""
"render" automatically looks for the views in "templates" folder of each app, i.e. "appQuart/templates"
"""
# Create your views here.

def index(request):
    return render(request,'index.html')

def tradingNewsApp(request):
    print('----------------Request:',str(request))
    return render(request,'trading_app_login.html')



