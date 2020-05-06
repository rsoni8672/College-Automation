from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
from django.db import models

# Create your models here.
class branchclass(models.Model):
    classname = models.CharField(max_length = 50)
    def __str__(self):
        return '%s' %( self.classname)
    class Meta:
        db_table = 'branchclass'


class student(models.Model):
    studentid  = models.ForeignKey(User, on_delete = models.CASCADE)
    contactnumber = models.CharField(max_length =10)
    branch = models.ForeignKey(branchclass,on_delete = models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return "%s %s %s %s " %(self.studentid,self.contactnumber, self.branch, self.email)

    class Meta:
        db_table  = "student"


class authority(models.Model):
    authorityid  = models.ForeignKey(User, on_delete = models.CASCADE)
    contactnumber = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)
    
    class Meta:
        db_table  = "authority"

    def __str__(self):
        return "%s %s %s " %(self.userid,  self.contactnumber, self.email)
    


