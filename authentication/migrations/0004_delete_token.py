# Generated by Django 4.0.4 on 2022-05-30 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_token_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]
