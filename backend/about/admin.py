from django.contrib import admin
from .models import AboutSection, Founder, TeamMember, TimelineEvent


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_type', 'order', 'is_published', 'created_at']
    list_filter = ['section_type', 'is_published', 'created_at']
    search_fields = ['title', 'content']
    ordering = ['order', 'created_at']


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'email', 'bio']
    ordering = ['-created_at']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'role', 'bio']
    ordering = ['order', 'name']


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'is_milestone', 'order', 'created_at']
    list_filter = ['is_milestone', 'event_date', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['event_date', 'order']
