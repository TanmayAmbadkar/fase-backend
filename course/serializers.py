import logging

from django.http import Http404
from users.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.fields import CurrentUserDefault
from attendance.models import Attendance
from course.models import Course

logger = logging.getLogger(__file__)


class CourseSerializer(serializers.ModelSerializer):
    instructors = UserSerializer(many=True, read_only=True)
    is_already_marked = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'course_code',
            'course_name',
            'semester',
            'academic_year',
            'instructors',
            'start_timestamp',
            'attendance_duration_in_minutes',
            'is_already_marked',
        )

    def get_is_already_marked(self, course):
        user = self.context.get('request').user

        attendance = Attendance.objects.filter(student=user, course=course,).exists() #TODO finish this query

        if not attendance:
            return False

        return True

    def create(self, validated_data):
        user = self.context['request'].user

        if 'instructors' in validated_data:
            _ = validated_data.pop('instructors')

        course = Course.objects.create(**validated_data)

        course.instructors.add(user.institute_email)

        return course

    def update(self, instance, validated_data):
        instance.course_name = validated_data.get(
            'course_name', instance.course_name)
        instance.course_code = validated_data.get(
            'course_code', instance.course_code)
        instance.semester = validated_data.get('semester', instance.semester)
        instance.academic_year = validated_data.get(
            'academic_year', instance.academic_year)
        instance.start_timestamp = validated_data.get(
            'start_timestamp', instance.start_timestamp)
        instance.attendance_duration_in_minutes = validated_data.get(
            'attendance_duration_in_minutes', instance.attendance_duration_in_minutes)

        instance.save()

        return instance
