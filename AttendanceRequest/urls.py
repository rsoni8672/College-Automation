from django.urls import path
from AttendanceRequest import views
urlpatterns = [
    path('attendance_application',views.attendance_application, name = "apply" ),
    path('check_attendance_hod', views.check_attendance_hod, name= "check_attendance_hod"),
    path('approve_attendance', views.approve_attendance, name = "Approve Attendance"),
    path('export_excel', views.export_excel , name  = "export excel"),
]
