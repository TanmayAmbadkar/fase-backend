# Generated by Django 4.0.5 on 2022-06-14 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_course_course_student_mapper_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_student_mapper_file',
            field=models.FileField(blank=True, null=True, upload_to='student_mapper_csv/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv', 'xlsx'])]),
        ),
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]