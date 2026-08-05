from django.contrib import admin
from .models import Forum, Topic, Post, Comment, Notification


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'author', 'is_pinned', 'created_at']
    list_filter = ['forum', 'is_pinned', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['topic', 'author', 'created_at']
    list_filter = ['topic', 'created_at']
    search_fields = ['content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    list_filter = ['post', 'created_at']
    search_fields = ['content']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'verb', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['verb', 'user__email']
