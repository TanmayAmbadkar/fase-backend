# Generated by Django 4.0.4 on 2022-05-29 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='course',
            name='course_unique_per_sem_per_year',
        ),
    ]
