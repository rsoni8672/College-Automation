from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import login, logout , authenticate 
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from CollegeAutomation.settings import*
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
#Alumni Site 
@csrf_exempt
def alumnihome2(request):
    userid = auth.get_user(request).id
    Alumni = alumni.objects.get(userid = userid)
    Experiences  = experience.objects.filter(alumniid  = Alumni)
    Friends  = alumni.objects.filter(branch = Alumni.branch, passoutyear = Alumni.passoutyear )
    print("Friends")
    return render(request, "AlumniTracking/alumnihome.html", {'Alumni':Alumni ,'experiences':Experiences, 'friends':Friends})


@csrf_exempt
def alumniregister(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        firstname  = request.POST.get('firstname')
        email = request.POST.get('email')
        password1  = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(password1, password2)
        contactnumber  = request.POST.get('contact')
        branch = request.POST.get('branch')
        passout_year  = request.POST.get('passoutyear')
        if User.objects.filter(username   = username).exists():
            return HttpResponse("Username Aldready exists")
        elif password1 != password2:
            return HttpResponse("Pasword Does not match the username") 
        else:
            user  = User.objects.create_user(username = username, email = email , first_name  = firstname, password= password1)
            user.save()
            Alumni  = alumni(userid = user, branch  = branch, contactnumber = contactnumber, email = email, passoutyear = passout_year )
            Alumni.save()
            return render( request , "AlumniTracking/login.html")
    else:
        return render(request, 'AlumniTracking/alumniregister.html')
@csrf_exempt
def alumnilogin(request):
    if request.method == "POST":
        username = request.POST.get('username')   
        password = request.POST.get('password')
        user  = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            Alumni = alumni.objects.get( userid = user.id )
        else:
            return HttpResponse("invalid Credentials")
        return redirect(alumnihome2)
    return render(request, "AlumniTracking/login.html")

def updateprofile(request):
    if request.method == "POST":
        organizationname  = request.POST.get('organizationname')
        position = request.POST.get('position')
        description = request.POST.get('description')
        joindate = request.POST.get('joindate')
        currentlyworking  = request.POST.get('workingpresently')
        userid = auth.get_user(request).id
        Alumni = alumni.objects.get(userid = userid )

        Experience  = experience(alumniid  = Alumni , organizationname = organizationname, position = position , description = description, 
        joindate = joindate , workingpresently = currentlyworking)
        Experience.save()
        return redirect(alumnihome2)
        #return render(request, "AlumniTracking/alumnihome.html", {'Alumni':Alumni ,'experiences':Experiences})
        return HttpResponse("Hello World Child ")

    return render(request , 'AlumniTracking/updateprofile.html')


#Admin Site
# def adminhome(request):
#     print("Hello world")
    
@csrf_exempt
def addannouncement(request):
    if request.method  == "POST":
        Name  = request.POST.get('Eventname')
        Description = request.POST.get('Description')
        print(Description)
        batch = request.POST.get('batchyear')
        batch = batch.split(',')
        Announcement  = announcement(announcement_name  = Name  , announcement_description = Description,  batchyear = batch)
        Announcement.save()
        recipient = []
        recievers = []
        for b in batch:
            #print(b)
            q = alumni.objects.filter(passoutyear = int(b))
            for b in q:
                recipient.append(b)
        
        for r in recipient:
            recievers.append(r.email)

        print(recievers)
        send_mail(Name,Description,EMAIL_HOST_USER,recievers)
        return HttpResponse("Done")
    else:
        return render(request, 'AlumniTracking/adminhome.html')
@csrf_exempt
def searchBatchMates(request):
    userid  = auth.get_user(request).id
    user  = User.objects.get(id = userid)
    Alumni = alumni.objects.get(userid = user)
    print(Alumni)
    branch =  Alumni.branch
    year = Alumni.passoutyear

    BatchMates = alumni.objects.filter(branch = branch, passoutyear = year)
    return render(request, 'AlumniTracking/batchmates.html', {'BatchMates':BatchMates}) 
@csrf_exempt    
def search_by_company(request):
    if request.method == "POST":
        company_name  = request.POST.get('companyname')
        Experience  = experience.objects.filter(organizationname  = company_name)
        print(Experience)
        return render(request, 'AlumniTracking/searchresults.html', {'Experience':Experience, 'CompanyName':company_name})
    
@csrf_exempt
def search_by_alumni(request):
    if request.method == "POST":
        Name  = request.POST.get('alumni_name')
        A = []
        print("Name ", Name)
        if(len(Name.split(' ')) >=2 ):
           Name = Name.split(' ')    
        if(len(Name) >= 2):
            user  = User.objects.filter( Q(first_name__contains = Name[0])|Q(last_name__contains  = Name[1]))
            print("User 1", user, len(user))
        else:
            user  = User.objects.filter(first_name__contains = Name)
            print("User 2" , user)
        for i in user:
            print(i.id)
            Alumni = alumni.objects.get(userid = i.id)
            print("Alumni", Alumni)
            A.append(Alumni)
        print("A",A)  
        return render(request, 'AlumniTracking/searchbyalumni.html', {'user':user, 'Alumnus':A})
    