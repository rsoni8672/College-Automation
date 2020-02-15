from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def studentlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')   
        password = request.POST.get('password')
        user  = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)

        else:
            return HttpResponse("invalid Credentials")
        return HttpResponse("Tdfndkdgx")
    

    return render(request, "Students/studentlogin.html")