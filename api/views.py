from rest_framework import viewsets
from rest_framework.response import Response
from .models import Students, Courses
from .serializers import CoursesSerializer, StudentSerializer


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()

    # Here we are overriding list method to list the data as a dictionary instead of array
    def list(self, request, *args, **kwargs):
        # Calling the original 'list'
        response = super(StudentViewset, self).list(request, *args, **kwargs)
        response_dict = {"Students" : response.data}
        response.data = response_dict
        return response

    # FOR POST REQUEST
    def create(self, request, *args, **kwargs):
        data = request.data
        create_student = Students.objects.create(name=data['name'], enrolled_courses=data['enrolled_courses'])
        create_student.save()

        for course in data['enrolled_courses']:
            course_obj = Courses.objects.get(course_name=course["course_name"])
            create_student.enrolled_courses.add(course_obj)

        serializer = StudentSerializer(create_student)
        return Response(serializer.data)


class CourseViewset(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

    # Here we are overriding list method to list the data as a dictionary instead of array
    def list(self, request, *args, **kwargs):
        # Calling the original 'list'
        response = super(CourseViewset, self).list(request, *args, **kwargs)
        response_dict = {"Courses" : response.data}
        response.data = response_dict
        return response