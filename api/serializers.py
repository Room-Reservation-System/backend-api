from rest_framework import serializers
from .models import *

class MeetingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'

class RoomSerializer (serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class CohortSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = '__all__'

class InstructorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class LectureSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'


class TargetMail(serializers.Serializer):
    email=serializers.CharField(max_length=300)