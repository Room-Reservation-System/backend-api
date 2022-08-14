from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Room (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    seats = models.IntegerField(default = 0,validators=[MaxValueValidator(250), MinValueValidator(1)])
    academic = models.BooleanField(default=False)
    information = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']


class Instructor (models.Model):
    name =   models.CharField(max_length=150)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Cohort (models.Model):
    major = models.CharField(max_length=2,choices=(('CS','Computer Science'),('CM','Communications and Media')), blank=False, default='cs')
    year = models.IntegerField(default = 2025)
    # classColor = models.CharField(max_length=300)

    def __str__(self):
        return str(self.major+' - '+str(self.year))
    class Meta:
        ordering = ['year']


class Lecture (models.Model):
    title = models.CharField(max_length=100)
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    cohort = models.ForeignKey('Cohort', on_delete=models.SET_NULL, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    WEEKDAYS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )
    day = models.CharField(
        max_length=1,
        choices=WEEKDAYS,
        default = '1',
        help_text='On Week day')

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError('Start time should be before the end time')
        return super().clean()

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['day']


class Meeting (models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
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


