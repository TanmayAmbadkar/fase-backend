# Generated by Django 4.0.5 on 2022-06-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
