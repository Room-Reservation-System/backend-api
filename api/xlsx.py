from models import Meeting
from datetime import date, timedelta
from serializers import MeetingSerializer, RoomSerializer


current_date = date.today()
end_date = current_date + timedelta(days=60)
start_date = current_date - timedelta(days=30)

if id == 0:
    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, many = True)
    print(serializer.data)

try:    
    meetings =  Meeting.objects.filter(room_id__id = 1, date__range=[start_date, end_date])
except Meeting.DoesNotExist:
    print("HTTP_404_NOT_FOUND")

serializer = MeetingSerializer(meetings, many = True)
print(serializer.data)