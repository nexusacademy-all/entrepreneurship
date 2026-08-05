from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Testimonial, SuccessStory
from .serializers import TestimonialSerializer, SuccessStorySerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['is_featured']


class SuccessStoryViewSet(viewsets.ModelViewSet):
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'excerpt', 'author_name']
    filterset_fields = ['is_published']
