from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name ="regisster"),
    path('authority', views.authorityregister, name  = 'authorityregister'),
    path('login', views.studentlogin, name = "studentlogin"),
    path('authoritylogin' , views.authoritylogin, name  = "authoritylogin"),
   

]