from rest_framework import serializers
from .models import Category, Tag, Article, Video, Download


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'featured_image', 'status', 'author', 'categories', 'tags', 'published_at', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'slug', 'description', 'video_url', 'thumbnail', 'status', 'published_at', 'created_at']
        read_only_fields = ['created_at']


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = ['id', 'title', 'slug', 'description', 'file', 'status', 'download_count', 'created_at']
        read_only_fields = ['created_at']
