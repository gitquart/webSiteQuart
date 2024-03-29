from django.urls import path

from . import views

#appQuart/urls : Define here the links to the views, views is the Controller, urls defines where to find any link in web site
#For example, if a href has "tradingApp" it will look for it here at first
urlpatterns = [
    path('', views.index,name='index'),
    path('tradingApp_login',views.tradingNewsApp_login,name='login_app'),
    path('tradingApp_register',views.tradingNewsApp_register,name='register_app'),
    path('login',views.login,name='login_process'),
    path('tradingApp',views.tradingNewsApp,name='tradingApp')
]