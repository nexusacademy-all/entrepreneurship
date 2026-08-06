from django.contrib import admin
from .models import MethodologySection


@admin.register(MethodologySection)
class MethodologySectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_type', 'order', 'is_published', 'created_at']
    list_filter = ['section_type', 'is_published', 'created_at']
    search_fields = ['title', 'content']
    ordering = ['order', 'created_at']
