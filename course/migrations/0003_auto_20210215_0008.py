# Generated by Django 3.1.6 on 2021-02-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210215_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='start_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
