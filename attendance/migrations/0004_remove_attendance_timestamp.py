# Generated by Django 4.0.4 on 2022-06-02 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='timestamp',
        ),
    ]
