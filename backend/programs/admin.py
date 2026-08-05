from django.contrib import admin
from .models import Program, Registration, Workshop, Webinar


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'start_date', 'end_date', 'price', 'capacity', 'status', 'created_at']
    list_filter = ['type', 'status', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'program', 'status', 'registered_at']
    list_filter = ['status', 'program', 'registered_at']
    search_fields = ['user__email', 'program__title']


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'date', 'time', 'price', 'capacity', 'status']
    list_filter = ['status', 'date']
    search_fields = ['title', 'description', 'instructor']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ['title', 'speaker', 'scheduled_at', 'price', 'status']
    list_filter = ['status', 'scheduled_at']
    search_fields = ['title', 'description', 'speaker']
    prepopulated_fields = {'slug': ('title',)}
