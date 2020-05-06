from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class KEY_AUTHORITY(models.Model):

    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    floor_assigned  = models.IntegerField()

    class Meta:
        db_table  = "KEY_AUTHORITY"
    def __str__(self):
        return "%s %s" %(self.userid, self.floor_assigned)

class ROOM(models.Model):
    room_number = models.IntegerField()
    room_type  = models.CharField(max_length = 15)
    class Meta:
        db_table = "ROOM"
    def __str__(self):
        return "%s %s" %(self.room_number , self.room_type)

class LECTURE_TIMINGS(models.Model):
    room_number = models.ForeignKey(ROOM, on_delete = "models.CASCADE")
    day = models.IntegerField()
    start_time  = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = "LECTURE_TIMINGS"
    def __str__(self):
        return "%s %s %s %s" %(self.room_number, self.day, self.start_time, self.end_time)

