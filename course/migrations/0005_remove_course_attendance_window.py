# Generated by Django 3.1.6 on 2021-02-15 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20210215_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='attendance_window',
        ),
    ]
