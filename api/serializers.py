from rest_framework import serializers
from .models import Meeting, Room, TargetMailUser

class MeetingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id','name','description','date','start_time','end_time','room','is_repeated','verify_id','email','status']

class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','name','information']

class TargetMail(serializers.Serializer):
    # class Meta:
    #     model=TargetMailUser
    # fields 
    email=serializers.CharField(max_length=300)
     