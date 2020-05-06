from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from registrations.models import *
from .models import *
from CollegeAutomation.settings import firebaseConfig
import datetime, itertools
import pyrebase
# Create your views here.
firebase = pyrebase.initialize_app(firebaseConfig)

Available = []
branch_dict = {
    1:6,2:4,3:5,4:3,5:4
}
db = firebase.database()
def apply(request):
    if request.method == "POST":
        n = 0
        rooms = []
        number_of_rooms = request.POST.get("number_of_rooms")
        requested_date = request.POST.get("date")
        purpose = request.POST.get("purpose")
        Start_time  = request.POST.get("StartTime")
        End_time = request.POST.get("EndTime")
        AC_requirement = request.POST.get("requirement_AC")
        All_rooms = db.child('Rooms').shallow().get().val()
        userid  = request.POST.get('localId')
        print(userid)
        print(requested_date)
        year, month, date = (int(x) for x in requested_date.split('-'))
        weekday = datetime.date(year, month, date).weekday() + 1
        # print("WeekDay", weekday)
        
        DaySchedule  = db.child('LectureTimings').child(weekday).shallow().get().val()
        #userid  = auth.get_user(request).id
        #user = User.objects.get(id = userid)
        Student =db.child('Users').child('Students').child(userid).get().val()#  student.objects.get(studentid = user)
        floor  = Student['Branch']
        #floor = branch_dict[branch]
                
        # print(" Start and End Time ",str(Start_time), str(End_time))
        # print("Student belongs to", floor)
        print("Day Schedule", DaySchedule)
        for i in DaySchedule:
            room_no = db.child('Rooms').child(i).child('room_no').get().val()
            end_time  = db.child('LectureTimings').child(weekday).child(i).child("EndTime").get().val()
            start_time = db.child('LectureTimings').child(weekday).child(i).child("StartTime").get().val()
            # print(" Start and End Time ",str(start_time), str(end_time))
            TS1 = [int(('').join(str(Start_time).split(':'))), int(('').join(str(End_time).split(':')))]
            TS2 = [int(('').join(str(start_time).split(':'))), int(('').join(str(end_time).split(':')))]
            if check(TS2, TS1) == True:
                Available.append(i)
        print(Available)
        for i in Available:
            Bookings  = db.child('Bookings').child(i).child(requested_date).shallow().get().val()
            print("Bookings", Bookings)
            if Bookings is None:
                rooms.append(db.child('Rooms').child(i).get().val()['room_no'])
            else:    
                for j in Bookings:
                    st  = db.child('Bookings').child(i).child(requested_date).child(j).get().val()['start_time']
                    print( " St", st)
                    et  = db.child('Bookings').child(i).child(requested_date).child(j).get().val()['end_time']
                    av = check([int(('').join(str(st).split(':'))), int(('').join(str(et).split(':')))],[int(('').join(str(Start_time).split(':'))), int(('').join(str(End_time).split(':')))])
                    if av == True:
                        rooms.append(db.child('Rooms').child(i).get().val()['room_no'])
                    if av == False:
                        if i in rooms:
                            rooms.remove(db.child('Rooms').child(i).get().val()['room_no'])
            print("Please select from these Rooms", rooms)
        return render(request, 'KeyPermission/application_portal.html', {'rooms':rooms, 
            "number_of_rooms":number_of_rooms,"date":requested_date,"purpose":purpose,'status':0 ,"StartTime":Start_time, "EndTime":End_time,"AC_requirement":AC_requirement
        ,'i':1, 'localId':userid   
            })
    localId = request.GET.get('localId')
    print(localId)
    return render(request, 'KeyPermission/application_portal.html', {'localId': localId})


def confirm(request):
    if request.method == "POST":
        number_of_rooms = request.POST.get("number_of_rooms")
        requested_date = request.POST.get("date")
        purpose = request.POST.get("purpose")
        Start_time  = request.POST.get("StartTime")
        End_time = request.POST.get("EndTime")
        AC_requirement = request.POST.get("requirement_AC")
        room_no = request.POST.get('room_no')
        userId = request.POST.get('localId')
        print("Obtained Query is ", number_of_rooms, requested_date, purpose, Start_time, End_time, AC_requirement, room_no)
        db.child('FinalBookings').push({
            'date':requested_date,
            'rooms':room_no,
            'start_time':Start_time,
            'end_time':End_time,
            'user_id':userId,
            'purpose':purpose,
                   'principal_approved':0,
            'Hod_approved':0
        })
        room_no = room_no.split(',')
        
        for i in room_no:
            print("i " ,int(i.strip()) )
            for j in db.child('Rooms').shallow().get().val():
                if str(db.child('Rooms').child(j).get().val()['room_no']) == str("".join(i.split())):
                    print("Adding to Db")
                    db.child('Bookings').child(j).child(str(requested_date)).push({
                        'userid':userId,
                        'purpose':purpose,
                        'start_time':Start_time,
                        'end_time':End_time,
                        
                    })

    return HttpResponse(" You have successfully completed the room bookings.")

def check(entry1, entry2):
    print(entry1 , entry2)
    if(entry1[0] == entry2[0] or entry1[1] == entry2[1]):
        return False
    if(entry1[0] > entry2[0]  and entry1[0] <entry2[1]):
        return False
    if(entry1[0]<entry2[0] and entry1[1] > entry2[0]):
        return False
    return True

def checklab(entry1, entry2):
    if(entry2[0] >= entry1[0] and entry2[1]<=entry1[1]):
        return True
    else:
        return  False

def apply_lab(request):
    if request.method=="POST":
        labs_list = request.POST.get('labs_list')
        requested_date  = request.POST.get('requested_date')
        start_time = request.POST.get('Start_Time')
        purpose = request.POST.get('purpose')
        end_time = request.POST.get('End_Time')
        Available_labs = []
        userId = request.POST.get('localId')
        labs_list = labs_list.split(',')
        print(labs_list)
        
        # labs = db.child('Labs').shallow().get().val()
        # print(labs)
        year, month, date = (int(x) for x in requested_date.split('-'))
        weekday = datetime.date(year, month, date).weekday() + 1
        DaySchedule = db.child('LabTimings').child(weekday).shallow().get().val()
        for i in DaySchedule:
            if str(db.child('Labs').child(i).child('lab_no').get().val()) in labs_list:                
                schedule  = db.child('LabTimings').child(weekday).child(i).shallow().get().val()
                for j in  schedule:
                    st = db.child('LabTimings').child(weekday).child(i).child(j).child('start_time').get().val()
                    et = db.child('LabTimings').child(weekday).child(i).child(j).child('end_time').get().val()
                    if checklab([int(st), int(et)], [int(('').join(str(start_time).split(':'))), int(('').join(str(end_time).split(':')))]):
                        Available_labs.append(i)
                        break
        rooms = []
        print(requested_date)
        print(Available_labs)
        for i in Available_labs:
            Bookings  = db.child('LabBookings').child(i).child(requested_date).shallow().get().val()
            print("Bookings", Bookings)
            if Bookings is None:
                rooms.append(db.child('Labs').child(i).get().val()['lab_no'])
            else:    
                for j in Bookings:
                    st  = db.child('LabBookings').child(i).child(requested_date).child(j).get().val()['start_time']
                    print( " St", st)
                    et  = db.child('LabBookings').child(i).child(requested_date).child(j).get().val()['end_time']
                    av = check([int(('').join(str(st).split(':'))), int(('').join(str(et).split(':')))],[int(('').join(str(start_time).split(':'))), int(('').join(str(end_time).split(':')))])
                    if av == True:
                        print("From Here")
                        rooms.append(db.child('Labs').child(i).get().val()['lab_no'])
                    if av == False:
                        if db.child('Labs').child(i).get().val()['lab_no'] in rooms:
                            rooms.remove(db.child('Labs').child(i).get().val()['lab_no'])
            print("Please select from these Rooms", rooms)

        print("Available Labs are", Available_labs)
        return render(request, 'KeyPermission/lab_application.html', {'labs':(',').join(labs_list), 
            "date":requested_date,"purpose":purpose,
            'status':0 ,"StartTime":start_time, "EndTime":end_time,'i':1,'rooms':rooms,'localId':userId }  )  
    else:
        localId = request.GET.get('localId')
        print(localId)
        return render(request, 'KeyPermission/lab_application.html', {'localId':localId})     
    
def confirm_lab(request):
    if request.method == "POST":
        confirmed_labs = request.POST.get('confirmed_labs')
        requested_date  = request.POST.get('requested_date')
        start_time = request.POST.get('Start_Time')
        purpose = request.POST.get('purpose')
        end_time = request.POST.get('End_Time')
        userId = request.POST.get('localId')
        print(start_time, end_time)
        db.child('FinalBookings').push({
            'date':requested_date,
            'rooms':confirmed_labs,
            'start_time':start_time,
            'end_time':end_time,
            'user_id':userId,
            'purpose':purpose,
            'principal_approved':0,
            'Hod_approved':0
        })
        for i in confirmed_labs.split(','):
            print(i)
            for j in db.child('Labs').shallow().get().val():
                
                if str(db.child('Labs').child(j).get().val()['lab_no']) == str(i):
                    print("Adding to Db")
                    db.child('LabBookings').child(j).child(str(requested_date)).push({
                        'userid':userId,
                        'purpose':purpose,
                        'start_time':start_time,
                        'end_time':end_time
                    })
    
        return HttpResponse("Completed")



def check_applications(request):
    Bookings = db.child('FinalBookings').shallow().get().val()
    Final_bookings = []
    for i in Bookings:
        if db.child('FinalBookings').child(i).child('principal_approved').get().val() == 0:
            f =db.child('FinalBookings').child(i).get().val()
            userid  = f['user_id']
            user  = User.objects.get(id  = userid)
            Student  = student.objects.get(studentid = userid)
                
            Final_bookings.append({
                'id':i,
                'user':user,
                'student':Student,
                'room_no':f['rooms'],
                'date':f['date'],
                'start_time':f['start_time'],
                'end_time':f['end_time'],
                'purpose':f['purpose']
            })
    print(Final_bookings)
    return render(request, 'KeyPermission/check_permission.html', {'FinalBookings':Final_bookings})


def approve(request):
    if request.method == "POST":
        id  = request.POST.get('id')
        booking = db.child('FinalBookings').child(id).update({'principal_approved':1})
        return redirect('/KeyPermission/check_applications')
    
