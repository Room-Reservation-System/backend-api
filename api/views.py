from datetime import date, timedelta
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from random import randint
from django.db.models import Q
from django.http import FileResponse
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .xlsxGenerator.tableGenerator import TableGenerator
from .xlsxGenerator.filter import Filter
import hashlib


# @api_view(['GET'])
# def QRcodeGenerator(request, id):
    
#     if request.method=='GET':

#         if id == 0:
#             meetings = Meeting.objects.all()
#             serializer = MeetingSerializer(meetings, many = True)
#             return Response(serializer.data)

#         try:    
#             meetings =  Meeting.objects.filter(Q(room__id = id) & Q(type__exact = ('class')))
            
#         except Meeting.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)

#         serializer = MeetingSerializer(meetings, many = True)
        

#         link='https://www.youtube.com/watch?v=tXsQJhoauxc'
#         name='demo'
#         QRcodeGenerator().getQRcode(fileName=f'{name}{id}',siteLink=link)
#         # table.setData()
#         # file=open(table.getFile(),'rb')
#         response=FileResponse(QRcodeGenerator().getQRcode(fileName=name,siteLink=link))

# @api_view(['GET'])
# def xlsxForCohorts(request, id):
    
#     try:    
#         lectures =  Lecture.objects.filter(cohort__id = id)
#         cohorts = Cohort.objects.filter(id=id)
#     except Lecture.DoesNotExist or Cohort.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
#     lectureData = LectureSerializer(lectures, many = True)
#     cohortData=CohortSerializer(cohorts, many = True)

#     mainData=Filter().filter(events=lectureData.data,header=cohortData.data)
#     table=TableGenerator(data=mainData).setDataClassMode()
#     file=open(table.getFile(),'rb')
#     response=FileResponse(file)
#     return response

@api_view(['GET'])
def xlsxForRoom(request, id):
    
    try:    
        lectures =  Lecture.objects.filter(room__id = id)
    except Lecture.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    lectureData = LectureSerializer(lectures, many = True).data
    roomData=Filter().filterRoom(roomData=lectureData)
    headerData=Filter().filterHeader(header=id)
    # return Response(headerData)
    table=TableGenerator(title=headerData)
    table.setDataRoomMode(data=roomData['dataList'])
    file=open(table.getFile(),'rb')
    response=FileResponse(file)
    return response

@api_view(['GET'])
def xlsxForFaculty(request, id):
    
    try:    
        lectures =  Lecture.objects.filter(instructor__id = id)
        faculty = Instructor.objects.filter(id = id)
    except Lecture.DoesNotExist or Instructor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    classes = LectureSerializer(lectures, many = True).data
    instructor = InstructorSerializer(faculty, many = True).data
    data=Filter().filterInstractor(classes=classes,instructor=instructor[0])

    table=TableGenerator(title=data['instructor'])
    table.setDataFaculty(data=data['classes'], )
    file=open(table.getFile(),'rb')
    response=FileResponse(file)
    return response


@api_view(['GET'])
def xlsxForCohort(request, id):
    idCS=id
    idCM=id
    if id%2:
        idCS+=1
    else:
        idCM-=1
        
    try:    
        lecturesForCS =  Lecture.objects.filter(cohort__id = idCS)
        lecturesForCM = Lecture.objects.filter(cohort__id = idCM)
        cohortCS = Cohort.objects.filter(id=idCS)
        cohortCM = Cohort.objects.filter(id=idCM)

    except Lecture.DoesNotExist or Cohort.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    filter=Filter()
    groupCS = LectureSerializer(lecturesForCS, many = True).data
    headerCS = CohortSerializer(cohortCS, many = True).data[0]
    dataCS=filter.filterRoom(roomData=groupCS,group=headerCS['major'])

    groupCM = LectureSerializer(lecturesForCM, many = True).data
    headerCM = CohortSerializer(cohortCM, many = True).data[0]
    dataCM=filter.filterRoom(roomData=groupCM,group=headerCM['major'])

    mergedData=filter.mergeData(dict1=dataCM,dict2=dataCS)
    title=filter.mergeHeader(dict1=headerCS,dict2=headerCM)
    table=TableGenerator(title=title,step=15)
    table.setDataCohortMode(data=mergedData,)
    file=open(table.getFile(),'rb')
    # return Response(mergedData)
    response=FileResponse(file)
    return response


@api_view(['GET', 'POST'])
def event_list(request, id):

    if request.method == 'GET':

        current_date = date.today()
        end_date = current_date + timedelta(days=90)
        start_date = current_date - timedelta(days=60)

        if id == 0:

            meetings = Meeting.objects.all()
            serializer = MeetingSerializer(meetings, many = True)
            return Response(serializer.data)

        try:    
            meetings =  Meeting.objects.filter(Q(room__id = id,status__exact = ('accepted')) & (Q(date__range=[start_date, end_date])))
        except Meeting.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = MeetingSerializer(meetings, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MeetingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            room = Room.objects.get(pk = id)

            message = Mail(
            from_email='ilkhom.c@outlook.com',
            to_emails="eku.ulanov@gmail.com",
            subject='A new event is creteated !',
            html_content=f'Recieved a new event request for {room}, go to https://ilkhom19.pythonanywhere.com/admin/ to "ACCEPT" or "DECLINE" the event')
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                sg.send(message)
            except Exception as e:
                return Response("Couldn't send email!", status=status.HTTP_408_REQUEST_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lecture_list(request, id):
    if id == 0:
        meetings = Lecture.objects.all()
        serializer = LectureSerializer(meetings, many = True)
        return Response(serializer.data)
    try:    
        meetings =  Lecture.objects.filter(room__id = id)
    except Lecture.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = LectureSerializer(meetings, many = True)
    return Response(serializer.data)



@api_view(['GET'])
def per_cohort(request, id):
    try:    
        lectures =  Lecture.objects.filter(cohort__id = id)
    except Lecture.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = LectureSerializer(lectures, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def per_instructor(request, id):
    try:    
        lectures =  Lecture.objects.filter(instructor__id = id)
    except Lecture.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = LectureSerializer(lectures, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def room_list(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def cohort_list(request):
    cohorts = Cohort.objects.all()
    serializer = CohortSerializer(cohorts, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def instructor_list(request):
    instructors = Instructor.objects.all()
    serializer = InstructorSerializer(instructors, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def sendMail(request):
    targetMail=TargetMail(data=request.data)

    if targetMail.is_valid():
        address=targetMail.data['email']
        password=f'{randint(1000,9999)}'
        salt = os.environ.get('SALT')
        hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        message = Mail(
            from_email='ilkhom.c@outlook.com',
            to_emails=address,
            subject='Email Verification for RRS',
            html_content=f'Your Secret code is: {password}')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
        except Exception as e:
            return Response("Couldn't send email!", status=status.HTTP_408_REQUEST_TIMEOUT)
        return Response([address,hashed_password], status=status.HTTP_200_OK)
    else: return Response(targetMail.errors)



# @api_view(['GET', 'PUT', 'DELETE'])
# def meeting_detail(request, id):

#     try:    
#        meeting =  Meeting.objects.get(pk=id)
#     except Meeting.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MeetingSerializer(meeting)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MeetingSerializer(meeting, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         meeting.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
