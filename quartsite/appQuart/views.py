from django.shortcuts import render
from django.http import HttpResponse

"""
"render" busca en automático las vistas en la carpeta "templates" dentro de cada app, ejemplo "appQuart->templates"
"""
# Create your views here.

def primis(request):
    return render(request,'index.html')
