from django.urls import path
from . import views
urlpatterns  = [
 path('apply_room', views.apply, name  = "Apply"),
 path('apply_lab', views.apply_lab , name = "Apply"),
 path('confirm', views.confirm, name= "Confirm"),
 path('confirm_lab', views.confirm_lab, name= "Lab Confirm"),
 path('check_applications', views.check_applications, name =  "Check BOokings"),
 path('approve', views.approve, name  = "Approve"),
 path('check_key_permission_hod', views.check_key_permission_hod, name  = "Approve_hod"),
 path('approve_hod', views.approve_hod, name = "approve hod"),
 path('approve_principal', views.approve_principal, name= "approve principal"),
]