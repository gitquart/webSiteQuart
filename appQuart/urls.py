from django.urls import path

from . import views

#appQuart/urls : Define here the links to the views, views is the Controller, urls defines where to find any link in web site
#For example, if a href has "tradingApp" it will look for it here at first
urlpatterns = [
    path('', views.index),
    path('tradingApp_login',views.tradingNewsApp_login),
    path('tradingApp_register',views.tradingNewsApp_register),
    path('login',views.login)
]