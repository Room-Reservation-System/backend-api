# Generated by Django 4.0.5 on 2022-07-02 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_meeting_date_meeting_email_meeting_end_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='room_id',
            new_name='room',
        ),
    ]
