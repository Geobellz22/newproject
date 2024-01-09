from django.urls import path
from .views import get_courses, create_course, get_course, update_course, delete_course

urlpatterns = [
    path('courses/', get_courses, name='get_courses'),
    path('create_course/', create_course, name='create_course'),
    path('courses/<int:pk>/', get_course, name='get_course'),
    path('courses/<int:pk>/update/', update_course, name='update_course'),
    path('courses/<int:pk>/delete/', delete_course, name='delete_course'),
]
