from . import views
from django.urls import path
urlpatterns = [

    path('login', views.alumnilogin , name  = "login"),
    path('register', views.alumniregister, name  = "register"),
    path('updateprofile',views.updateprofile, name  = "updateprofile"),
    path('alumnihome', views.alumnihome2,name = "alummnihome"),
    path('addannouncement', views.addannouncement, name  = "addannouncement"),
    
]