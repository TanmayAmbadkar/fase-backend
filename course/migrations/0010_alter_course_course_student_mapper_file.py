# Generated by Django 4.0.5 on 2022-06-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_course_student_mapper_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_student_mapper_file',
            field=models.FileField(blank=True, null=True, upload_to='student_mapper_csv/'),
        ),
    ]