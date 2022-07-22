# Generated by Django 4.0.5 on 2022-07-21 14:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_meeting_verify_id_alter_meeting_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='seats',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(1)]),
        ),
    ]