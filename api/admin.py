from django.contrib import admin
from .models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','academic','seats','information','id']

class CohortAdmin(admin.ModelAdmin):
    list_display = ['year','major']

class InstructorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Instructor._meta.fields if field.name != "id"]

class LectureAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Lecture._meta.fields if field.name != "id"]

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['title','description','room','status','date','start_time','end_time','email','created_at']
    list_filter =  ('status','room')

admin.site.register(Room,RoomAdmin)
admin.site.register(Cohort,CohortAdmin)
admin.site.register(Lecture,LectureAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Meeting, MeetingAdmin)