from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from CollegeAutomation.settings import firebaseConfig
import uuid
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import datetime
firebase= pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage  = firebase.storage()

def attendance_application(request):
    if request.method=="POST":
        Competition_Name = request.POST.get('Competition_Name')
        Organization_Name = request.POST.get('Organization_Name')
        Start_Date = request.POST.get('Start_date')
        End_date = request.POST.get('End_date')
        presence_proof = request.FILES['Attendance_Proof']
        userId = request.POST.get('localId')
        print(presence_proof)
        uid = uuid.uuid1()
        P = storage.child('Images/'+str(uid)).put(presence_proof)
        print(P)
        db.child('Attendance').child('Requests').push({
            'CompetitonName':Competition_Name,
            'Organization_Name':Organization_Name,
            'Start_Date':Start_Date,
            'End_Date':End_date,
            'presence_proof':storage.child('Images/'+str(uid)).get_url(None),
            'dean_status':0,
            'userId':userId,
            'General_Secratary_status':0  
        })
        # Fetch the service account key JSON file contents


        # Initialize the app with a service account, granting admin privileges
        
        return HttpResponse("Done")
    localId  = request.GET.get('localId')
    print(localId)
    return render(request,'Attendancerequest/request_competition_Attendance.html', {'localId':localId})


# Create your views here.
