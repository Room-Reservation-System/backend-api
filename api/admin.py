from django.contrib import admin
from .models import Meeting, Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','academic','seats','information','id']

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['title','description','room','type','status','date','start_time','end_time','email','created_at']
    list_filter = ( 'room','type','date','status')

admin.site.register(Room,RoomAdmin)
admin.site.register(Meeting, MeetingAdmin)