from django.contrib import admin
from .models import Meeting, Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','information','id']

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['name','description','room','date','start_time','end_time','is_repeated','email','status','created_at']
    list_filter = ( 'room','is_repeated','date','status')

admin.site.register(Room,RoomAdmin)
admin.site.register(Meeting, MeetingAdmin)