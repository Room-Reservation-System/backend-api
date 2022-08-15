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
    path('downloadxlsxclassmode/<int:id>', downloadXlsxClassMode), #needs an id (class) as a arg
    path('downloadxlsxcohortmode/<int:id>', downloadXlsxCohortMode),
    # path('qr/<int:id>',QRcodeGenerator)


]

