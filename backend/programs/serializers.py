from rest_framework import serializers
from .models import Program, Registration, Workshop, Webinar


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'title', 'slug', 'description', 'type', 'start_date', 'end_date', 'price', 'capacity', 'status', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'user', 'program', 'status', 'registered_at', 'notes']
        read_only_fields = ['registered_at']


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['id', 'title', 'slug', 'description', 'instructor', 'date', 'time', 'duration', 'price', 'capacity', 'status', 'created_at']
        read_only_fields = ['created_at']


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['id', 'title', 'slug', 'description', 'speaker', 'scheduled_at', 'duration', 'price', 'status', 'recording_url', 'created_at']
        read_only_fields = ['created_at']
