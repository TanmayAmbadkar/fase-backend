# Generated by Django 4.0.4 on 2022-06-09 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_coursewindowrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursewindowrecord',
            old_name='timestamp',
            new_name='start_timestamp',
        ),
    ]