from django.contrib import admin
from .models import Step, Tool, Resource, Exercise


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['step_number', 'title', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tools', 'resources', 'exercises']


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'created_at']
    search_fields = ['name', 'description']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'created_at']
    search_fields = ['name', 'description']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']
