from django.contrib import admin

from core.apps.courses.models import Course


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
