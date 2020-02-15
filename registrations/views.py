from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        firstname  = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1  = request.POST.get('password1')
        password2 = request.POST.get('password2')
        comtactnumber  = request.POST.get('contactnumber')
        if User.objects.get(username   = username).exists():
            return HttpResponse("Username Aldready exists")
        elif password1 != password2:
            return HttpResponse("Pasword Does not match the username") 
        else:
            user  = User.objects.create_user(username = username, email = email , first_name  = firstname, last_name = lastname, password= passsword1)
            user.save()
            return HttpResponse("Success")
    else:
        return render(request, 'register.html' )

def login(request):
    return HttpResponse("zsjfvgasjfas")

