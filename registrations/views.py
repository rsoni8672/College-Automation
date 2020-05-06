from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from .models import *
import pyrebase
# Create your views here.
from CollegeAutomation.settings import firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
def register(request):
    Branch_DICT = {'COMPS':6, 'IT':4, 'ETRX':3, 'EXTC':5, 'MCA':4}
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
        print(branch)
        # if User.objects.filter(username = username).exists():
        #     return HttpResponse("Username Aldready exists")
        if password1 != password2:
            return HttpResponse("Pasword Does not match the username") 
        else:
            user  = auth.create_user_with_email_and_password(email, password1)
            print(user)
            # user  = User.objects.create_user(username = username, email = email , first_name  = firstname, password= password1)
            # user.save()
            db.child('Users').child('Students').child(user['localId']).set({
              'First_Name': firstname,
              'Email':email,
              'Current_Year':current_year,
              'Contact_Number':comtactnumber,
              'Branch':Branch_DICT[branch],
            })
            # branch = branchclass.objects.get(classname  = branch)
            # Student  = student(studentid = user, branch  = branch, contactnumber = comtactnumber, email = email)
            # Student.save()
            return render( request , "registrations/studentlogin.html")
    else:
        return render(request, 'registrations/studentregister.html' )
        

def authorityregister(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        firstname  = request.POST.get('firstname')
        email = request.POST.get('email')
        password1  = request.POST.get('password')
        password2 = request.POST.get('password2')
        department  = request.POST.get('department')
        is_faculty  = request.POST.get('hod')
        print(is_faculty)
        classteacher = request.POST.get('classteacher')
        print(classteacher)
        print(password1, password2)
        comtactnumber  = request.POST.get('contact')
        if password1 != password2:
            return HttpResponse("Pasword Does not match the username") 
        # if User.objects.filter(username   = username).exists():
        #     return HttpResponse("Username Aldready exists")

        else:
            user  =auth.create_user_with_email_and_password(email, password1)
            if str(is_faculty) == 'class_teacher':
                pass
                db.child('Users').child('Authorities').child('Class_Teachers').child(user['localId']).set({
                    'User_Name':username,
                    'First_Name' : firstname,
                    'Email':email,
                    'Department':department,
                    'Class_Teacher_Of':classteacher,
                    'Contact_Number':comtactnumber
                })
                #Add to Faculty Table 
            elif str(is_faculty) == 'hod':
                db.child('Users').child('Authorities').child('HOD').child(user['localId']).set({
                    'User_Name':username,
                    'First_Name' : firstname,
                    'Email':email,
                    'Department':department,
                    'Contact_Number':comtactnumber
                })
            # user  = User.objects.create_user(username = username, email = email , first_name  = firstname, password= password1 ,is_staff = 1)
            # user.save()
            # branch = branchclass.objects.get(classname  = classteacher)
            # Authority  = authority(authorityid = user,  contactnumber = comtactnumber, email = email )
            # Authority.save()
            return render(request, 'registrations/authoritylogin.html')
    else:
        return render(request, 'registrations/authorityregister.html' )

@csrf_exempt
def studentlogin(request):
    Branch_DICT = {6:'COMPS', 4:'IT', 3:'ETRX', 5:'EXTC', 7:'MCA'}
    if request.method == "POST":
        username = request.POST.get('username')   
        password = request.POST.get('password')
        user = auth.sign_in_with_email_and_password(username, password)
        print(user)
        # user  = authenticate(username = username , password = password)
        if user is not None:
            bookings = db.child('FinalBookings').shallow().get().val()
            My_bookings = []  
            StudentName = db.child('Users').child('Students').child(user['localId']).get().val()['First_Name']
            StudentDepartment = Branch_DICT[db.child('Users').child('Students').child(user['localId']).get().val()['Branch'] ]
            Contact_Number= db.child('Users').child('Students').child(user['localId']).get().val()['Contact_Number']
            Email =  db.child('Users').child('Students').child(user['localId']).get().val()['Email']  
            for i in bookings:
                if (db.child('FinalBookings').child(i).child('user_id').get().val()) == (user['localId']):
                    # print(user.id)
                    f = db.child('FinalBookings').child(i).get().val()
                    My_bookings.append({
                        'id':i,
                    'user':user['localId'],
                    'Student_Name':StudentName,
                    'Student_Department':StudentDepartment,
                    'Contact':Contact_Number,
                    'Email':Email,
                    'room_no':f['rooms'],
                    'date':f['date'],
                    'start_time':f['start_time'],
                    'end_time':f['end_time'],
                    'purpose':f['purpose'],
                    'principal_approved':f['principal_approved'],
                    'hod_approved':f['Hod_approved']                })
            
            print(My_bookings)
            return render(request, 'registrations/student_home.html', {'FinalBookings':My_bookings, 'localId': user['localId'] })
            
            
        else:
            return HttpResponse("invalid Credentials")
    return render(request, "registrations/studentlogin.html")

def authoritylogin(request):
    if request.method == "POST":
        username = request.POST.get('username')   
        password = request.POST.get('password')
        user  = auth.sign_in_with_email_and_password(username, password)
        print(user['localId'])
        if( user['localId'] in db.child('Users').child('Authorities').child('Principal').shallow().get().val()):
            print("Principal Detected")
            return render(request, 'registrations/principal_home.html')
        if(user['localId'] in db.child('Users').child('Authorities').child('HOD').shallow().get().val()):
            Attendance_Applications = db.child()
            print("HOD DETECTED")
            return render(request, 'registrations/hod_home.html')
        if(user['localId'] in db.child('Users').child('Authorities').child('Class_Teachers').shallow().get().val()):
            print("HOD DETECTED")
            return render(request, 'registrations/hod_home.html')
        return HttpResponse("Tdfndkdgx")
    return render(request, "registrations/authoritylogin.html")



