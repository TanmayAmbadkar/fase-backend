# Generated by Django 4.0.4 on 2022-05-29 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('device_id', models.CharField(max_length=16)),
                ('is_physical', models.BooleanField(default=True)),
                ('is_rooted', models.BooleanField(default=False)),
                ('fingerprint', models.CharField(max_length=150)),
                ('sdk_int', models.IntegerField()),
                ('app_version_string', models.CharField(max_length=10)),
                ('app_build_number', models.IntegerField()),
                ('ssid', models.CharField(max_length=32)),
                ('bssid', models.CharField(max_length=23)),
                ('local_ip', models.GenericIPAddressField()),
                ('attendance_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('server_key', models.CharField(max_length=40)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
