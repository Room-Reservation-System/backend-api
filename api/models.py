from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# def filePath(instance,filename):
#     path='documents/'
#     format=f'upload {filename}'
#     return path.join(path, format)

# class FileHandler(models.Model): 
#     fileApload = models.FileField(upload_to=filePath)
#     def __str__(self):
#         return f'{self.fileApload}'

class TargetMailUser(models.Model):
    mail=models.CharField(max_length=300)

    def __str__(self): return self.mail
class Room (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    seats = models.IntegerField(default = 0,validators=[MaxValueValidator(250), MinValueValidator(1)])
    information = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']

class Meeting (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=5,choices=(('class','Class'),('event','Event')), blank=False, default='event')
    email = models.EmailField(null=True)

    MEETING_STATUS = (
        ('pending', 'Pending'),
        ('declined', 'Declined'),
        ('accepted', 'Accepted'),
    )
    status = models.CharField(
        max_length=8,
        choices=MEETING_STATUS,
        default = 'pending',
        help_text='Meeting status')

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('Start time should be before the end time')
        return super().clean()

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['date', 'start_time']
