from rest_framework import serializers
from .models import Step, Tool, Resource, Exercise


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'step_number', 'title', 'slug', 'description', 'content', 'tools', 'resources', 'exercises', 'is_published', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'description', 'file', 'link', 'created_at']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'file', 'link', 'created_at']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'title', 'description', 'instructions', 'created_at']
