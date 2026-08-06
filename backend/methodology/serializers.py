from rest_framework import serializers
from .models import MethodologySection


class MethodologySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodologySection
        fields = ['id', 'section_type', 'title', 'content', 'order', 'featured_image', 'is_published', 'created_at']
        read_only_fields = ['created_at']
