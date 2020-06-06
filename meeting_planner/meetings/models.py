from django.db import models
from datetime import time
# Create your models here.

class Room(models.Model):
    name            = models.CharField(max_length=50)
    floor           = models.IntegerField()
    room_number     = models.IntegerField()

    def __str__(self):
        return str(self.room_number)


class Meeting(models.Model):
    title           = models.CharField(max_length=200)
    date            = models.DateField()
    start_time      = models.TimeField(default=time(9))
    duration        = models.IntegerField(default=1)
    room            = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='meeting_room',default=None)
