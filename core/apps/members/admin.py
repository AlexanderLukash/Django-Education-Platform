from django.contrib import admin

from core.apps.members.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'created_at', 'updated_at')
    search_fields = ('phone',)
