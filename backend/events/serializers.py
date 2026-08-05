from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'slug', 'description', 'date', 'time', 'location', 'type', 'price', 'capacity', 'status', 'image', 'created_at']
        read_only_fields = ['created_at']
