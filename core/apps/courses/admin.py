from django.contrib import admin

from core.apps.courses.models import (
    Course,
    CourseReviewModel,
)


class CourseReviewInline(admin.TabularInline):
    model = CourseReviewModel
    extra = 0
    readonly_fields = ('member', 'rating', 'text')


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_visible')
    inlines = (CourseReviewInline,)


@admin.register(CourseReviewModel)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'course', 'is_approved')
    list_select_related = ('member', 'course')
