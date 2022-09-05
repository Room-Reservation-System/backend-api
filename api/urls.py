from django.urls import path
from .views import *

urlpatterns = [
  
    path('rooms/', room_list),
    path('events/<int:id>', event_list),
    path('lectures/<int:id>', lecture_list),    

    path('cohorts/', cohort_list),
    path('cohort/<int:id>', per_cohort),

    path('instructors/', instructor_list),
    path('instructor/<int:id>', per_instructor),

    path('mail/', sendMail),            

    path('downloadcohorts/<int:id>', xlsxForCohorts),
    path('downloadcohort/<int:id>', xlsxForCohort),
    path('downloadroom/<int:id>', xlsxForRoom),
    path('downloadfaculty/<int:id>', xlsxForFaculty),
    path('qr/<int:id>',getQRcode),


    path('demo/<int:id>',check)


]

