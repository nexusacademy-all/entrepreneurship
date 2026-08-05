from rest_framework import serializers
from .models import Testimonial, SuccessStory


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'content', 'avatar', 'is_featured', 'created_at']
        read_only_fields = ['created_at']


class SuccessStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'image', 'author_name', 'is_published', 'created_at']
        read_only_fields = ['created_at']
