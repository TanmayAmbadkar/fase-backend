# Generated by Django 4.0.4 on 2022-05-29 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_course_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='instructor',
            new_name='instructors',
        ),
    ]
