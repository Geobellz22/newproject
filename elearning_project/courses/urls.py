from django.urls import path
from .views import get_courses, create_course

urlpatterns = [
    path('courses/', get_courses, name='get_courses'),
    path('course/create/', create_course, name='create_course')
]
