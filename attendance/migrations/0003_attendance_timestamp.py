# Generated by Django 4.0.4 on 2022-06-02 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20220602_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]