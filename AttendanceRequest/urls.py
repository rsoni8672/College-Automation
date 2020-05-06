from django.urls import path
from AttendanceRequest import views
urlpatterns = [
    path('attendance_application',views.attendance_application, name = "apply" )
]