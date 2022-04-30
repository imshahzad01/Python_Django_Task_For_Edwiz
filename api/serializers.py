from rest_framework import serializers
from api.models import Students, Courses


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'course_name', 'source')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'name', 'enrolled_courses')
        depth = 1