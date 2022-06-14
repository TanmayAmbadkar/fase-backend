# Generated by Django 4.0.5 on 2022-06-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_section'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='course',
            name='course_unique_per_sem_per_year',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='course',
            name='course_student_mapper_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('course_code', 'semester', 'section', 'academic_year'), name='course_unique_per_sem_per_year_per_section'),
        ),
    ]
