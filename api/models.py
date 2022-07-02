from django.db import models


class Room (models.Model):
    name = models.CharField(max_length=150)
    information = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Meeting (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    is_repeated = models.BooleanField(null=True)
    verify_id = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    status = models.BooleanField(null=True)

    def __str__(self):
        return self.name
