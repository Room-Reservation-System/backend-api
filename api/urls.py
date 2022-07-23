from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:id>', views.meeting_list), # GET, POST   -->  id = class_id
    path('meeting/<int:id>', views.meeting_detail), # GET, PUT, DELETE -->  id = meeting_id
    path('rooms/', views.room_list),
    path('mail/', views.sendMail),              # GET rooms
    path('qwe/<int:id>', views.xlsxCheck),
]

