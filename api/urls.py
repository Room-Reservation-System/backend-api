from django.urls import path
from .views import *

urlpatterns = [
  
    path('room/<int:id>', meeting_list), # GET, POST   -->  id = class_id
    path('meeting/<int:id>', meeting_detail), # GET, PUT, DELETE -->  id = meeting_id
    path('rooms/', room_list), # GET rooms
    path('mail/', sendMail),             
    path('download/<int:id>', downloadFile), #needs an id (class) as a arg
    path('qr/<int:id>',QRcodeGenerator)
]

