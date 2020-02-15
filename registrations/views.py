from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def register(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        firstname  = request.POST.get('firstname')
        email = request.POST.get('email')
        current_year = request.POST.get('class')
        password1  = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(password1, password2)
        comtactnumber  = request.POST.get('contact')
        branch = request.POST.get('class')
        if User.objects.filter(username   = username).exists():
            return HttpResponse("Username Aldready exists")
        elif password1 != password2:
            return HttpResponse("Pasword Does not match the username") 
        else:
            user  = User.objects.create_user(username = username, email = email , first_name  = firstname, password= password1)
            user.save()
            branch = branchclass.objects.get(classname  = branch)
            Student  = student(studentid = user, branch  = branch, contactnumber = comtactnumber, email = email )
            Student.save()
            return render( request , "Authority/authoritylogin.html")
    else:
        return render(request, 'registrations/authorityregister.html' )
        

def authorityregister(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        firstname  = request.POST.get('firstname')
        email = request.POST.get('email')
        classteacher = request.POST.get('classteacher')
        password1  = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(password1, password2)
        comtactnumber  = request.POST.get('contact')
        
        if User.objects.filter(username   = username).exists():
            return HttpResponse("Username Aldready exists")
        elif password1 != password2:
            return HttpResponse("Pasword Does not match the username") 
        else:
            user  = User.objects.create_user(username = username, email = email , first_name  = firstname, password= password1 ,is_staff = 1)
            user.save()
            branch = branchclass.objects.get(classname  = classteacher)
            Authority  = authority(authorityid = user, classteacher = branch, contactnumber = comtactnumber, email = email )
            Authority.save()
            return render( request , "Authority/authoritylogin.html")
    else:
        return render(request, 'registrations/authorityregister.html' )



