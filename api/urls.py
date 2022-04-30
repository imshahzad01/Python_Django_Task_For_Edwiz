from django.urls import include, path
from .views import StudentViewset, CourseViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("student", StudentViewset, basename="student")
router.register("course", CourseViewset, basename="course")

urlpatterns = [
    path('', include(router.urls))
]