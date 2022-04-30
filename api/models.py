from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


class Students(models.Model):
    name = models.CharField(max_length=50)
    enrolled_courses = models.ManyToManyField(Courses)

    def __str__(self):
        return self.name