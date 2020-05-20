from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class alumni(models.Model):
    userid  = models.ForeignKey(User, on_delete = models.CASCADE)
    contactnumber = models.CharField(max_length  = 10)
    branch = models.CharField(max_length = 50)
    passoutyear = models.IntegerField()
    authorized = models.IntegerField(default  = 0 )
    email  = models.EmailField(max_length = 100)

    def __str__(self):
        return "%s %s %s %s %s " %(self.userid, self.contactnumber, self.branch ,self.passoutyear, self.authorized)
    class Meta:
        db_table  = "alumni"

class experience(models.Model):
    alumniid = models.ForeignKey(alumni, on_delete = models.CASCADE)
    organizationname = models.CharField(max_length  = 100)
    position = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    joindate  = models.DateField(auto_now_add=False)
    workingpresently = models.CharField(max_length =10)

    def __str__(self):
        return "%s %s %s %s %s" %(self.alumniid, self.organizationname, self.description , self.joindate, self.workingpresently)

    class Meta:
        db_table = "experience"


class announcement(models.Model):
    announcement_name  = models.CharField(max_length = 200)
    announcement_description = models.CharField(max_length = 500)
    adding_date  = models.DateField(auto_now_add=True)
    batchyear = models.CharField(max_length=100, default = "2020")
    class Meta:
        db_table  = 'announcement'
    def __str__(self):
        return '%s %s %s %s' %(self.announcement_name, self.announcement_description, self.adding_date, self.batchyear)
