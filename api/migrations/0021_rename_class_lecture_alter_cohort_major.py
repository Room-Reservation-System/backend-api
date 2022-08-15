# Generated by Django 4.0.5 on 2022-08-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_cohort_instructor_remove_meeting_type_class'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Lecture',
        ),
        migrations.AlterField(
            model_name='cohort',
            name='major',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('CM', 'Communications and Media')], default='cs', max_length=2),
        ),
    ]