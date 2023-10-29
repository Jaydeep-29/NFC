from django import views
from django.contrib import admin
from django.urls import path
from nfc_web import views

urlpatterns = [
    # path('', views.home),
    path('', views.login_view, name="login_view"),
    # path('login_view/', views.login_view, name="login_view"),
    path('nfc/', views.nfc, name="nfc"),
    
    
    
]