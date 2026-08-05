from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'slug', 'description', 'file', 'file_type', 'download_count', 'is_free', 'created_at']
        read_only_fields = ['created_at']
