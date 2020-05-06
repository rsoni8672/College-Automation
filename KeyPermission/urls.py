from django.urls import path
from . import views
urlpatterns  = [
 path('apply_room', views.apply, name  = "Apply"),
 path('apply_lab', views.apply_lab , name = "Apply"),
 path('confirm', views.confirm, name= "Confirm"),
 path('confirm_lab', views.confirm_lab, name= "Lab Confirm"),
 path('check_applications', views.check_applications, name =  "Check BOokings"),
 path('approve', views.approve, name  = "Approve"),
]