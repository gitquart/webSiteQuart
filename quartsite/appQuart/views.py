from django.shortcuts import render
from django.http import HttpResponse
import views

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the quart index.")
