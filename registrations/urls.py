from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name ="regisster"),
    path('login', views.login, name= "login"),

]