from django.db import models
from course.models import Course

from registration.models import BasicData

class Attendance(BasicData):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance_id = models.AutoField(primary_key=True, unique=True)
    server_key = models.CharField(max_length=40)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return "Course: "+str(self.course)+'\nAttendance Id: '+str(self.attendance_id)

