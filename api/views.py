from datetime import date, timedelta
from rest_framework.response import Response
from .serializers import MeetingSerializer, RoomSerializer, TargetMail
from .models import Meeting, Room
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from random import randint



@api_view(['GET', 'POST'])
def meeting_list(request, id):

    if request.method == 'GET':

        current_date = date.today()
        end_date = current_date + timedelta(days=60)
        start_date = current_date - timedelta(days=30)

        if id == 0:

            meetings = Meeting.objects.all()
            serializer = MeetingSerializer(meetings, many = True)
            return Response(serializer.data)

        try:    
            meetings =  Meeting.objects.filter(room_id__id = id, date__range=[start_date, end_date])
        except Meeting.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = MeetingSerializer(meetings, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MeetingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def meeting_detail(request, id):

    try:    
       meeting =  Meeting.objects.get(pk=id)
    except Meeting.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def room_list(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def sendMail(request):

    if request.method=='POST':
        targetMail=TargetMail(data=request.data)

        if targetMail.is_valid():
            userMail=targetMail.data['email']
            PINcode=f'{randint(1000,9999)}'
            
            html_temp = render_to_string('check_mail.html', {'PIN_code': PINcode})
            
            email = EmailMessage(
                "Checking django!",
                html_temp,
                settings.EMAIL_HOST_USER,
                [userMail]
                )

            email.fail_silently = False
            email.send()
            return Response(f'{PINcode=}, {userMail=}', status=status.HTTP_201_CREATED)
        else: return Response(targetMail.errors)


# {"email": "eku.ulanov@gmail.com"}