from django.urls import path
from .views import *

urlpatterns = [
  
    path('rooms/', room_list),
    path('cohorts/', cohort_list),
    path('instructors/', instructor_list),
    path('events/<int:id>', meeting_list),
    path('lectures/<int:id>', lecture_list), 
    path('mail/', sendMail),             
    path('download/<int:id>', downloadFile), 
]

