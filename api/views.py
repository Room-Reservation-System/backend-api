from datetime import date, timedelta
from rest_framework.response import Response
from .serializers import MeetingSerializer, RoomSerializer, TargetMail
from .models import Meeting, Room
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from random import randint
from django.db.models import Q

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
            meetings =  Meeting.objects.filter(Q(room__id = id) & (Q(date__range=[start_date, end_date]) | Q(type__exact = ('class'))))
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

    targetMail=TargetMail(data=request.data)

    if targetMail.is_valid():
        address=targetMail.data['email']
        password=f'{randint(1000,9999)}'
        html_temp = render_to_string('check_mail.html', {'PIN_code': password})
        
        email = EmailMessage(
            "Verify your Email",
            html_temp,
            settings.EMAIL_HOST_USER,
            [address]
            )

        email.fail_silently = False
        email.send()
        return Response(password, status=status.HTTP_200_OK)
    else: return Response(targetMail.errors)
