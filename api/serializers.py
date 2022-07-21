from rest_framework import serializers
from .models import Meeting, Room

class MeetingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id','title','description','date','start_time','end_time','room','type','email','status']

class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','seats','information']