from django.contrib import admin
from .models import Meeting, Room

# Register your models here.

#admin.site.register(Meeting)
#admin.site.register(Room)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','information','id']
    pass

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['name','description','room','date','start_time','end_time','is_repeated','email','status','created_at']
    list_filter = ( 'room','date','status')
    
    pass

admin.site.register(Room,RoomAdmin)
admin.site.register(Meeting, MeetingAdmin)