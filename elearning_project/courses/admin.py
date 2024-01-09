from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at', 'updated_at')
    search_fields = ('title', 'instructor__username')

admin.site.register(Course, CourseAdmin)
