from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:id>', views.meeting_list), # GET, POST   :: id = class_id
    path('meeting/<int:id>', views.meeting_detail), # PUT, DELETE :: id = meeting_id
    path('rooms/', views.room_list),                # GET rooms
]