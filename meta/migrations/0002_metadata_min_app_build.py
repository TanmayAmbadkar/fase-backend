# Generated by Django 3.1.6 on 2021-02-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='min_app_build',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]