# Generated by Django 4.0.4 on 2022-05-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('min_app_build', models.IntegerField(primary_key=True, serialize=False)),
                ('min_app_version', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Meta Data',
                'ordering': ['-min_app_build'],
            },
        ),
    ]
