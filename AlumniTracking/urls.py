from . import views
from django.urls import path
urlpatterns = [

    path('login', views.alumnilogin , name  = "login"),
    path('register', views.alumniregister, name  = "register"),
    path('updateprofile',views.updateprofile, name  = "updateprofile"),
    path('alumnihome', views.alumnihome2,name = "alummnihome"),
    path('addannouncement', views.addannouncement, name  = "addannouncement"),
    path("searchbatchmates" , views.searchBatchMates, name = "Search Batch MAtes"),
    path('search_by_company', views.search_by_company, name = "search"),
    path('search_by_alumni', views.search_by_alumni, name  = "search_by_alumni")
]