# Generated by Django 4.0.4 on 2022-05-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_course_academic_year'),
        ('users', '0002_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.course'),
        ),
    ]
