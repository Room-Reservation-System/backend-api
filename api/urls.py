from django.urls import path
from .views import *

urlpatterns = [
    # path('upload/', FileView.as_view(), name='file-upload'),
    path('room/<int:id>', meeting_list), # GET, POST   -->  id = class_id
    path('meeting/<int:id>', meeting_detail), # GET, PUT, DELETE -->  id = meeting_id
    path('rooms/', room_list),
    path('mail/', sendMail),              # GET rooms
    path('qwe/<int:id>', xlsxCheck),
]

