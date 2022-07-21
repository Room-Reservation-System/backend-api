# Generated by Django 4.0.5 on 2022-07-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_room_id_meeting_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Pending'), ('d', 'Declined'), ('a', 'Accepted')], default='p', help_text='Book availability', max_length=1),
        ),
    ]