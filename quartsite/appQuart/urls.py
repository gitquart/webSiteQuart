from django.urls import path

from . import views

urlpatterns = [
    path('', views.primis,name='index'),
]