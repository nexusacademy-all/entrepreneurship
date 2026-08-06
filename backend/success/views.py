from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import TemplateView
from .models import Testimonial, SuccessStory
from .serializers import TestimonialSerializer, SuccessStorySerializer


class SuccessStoryListView(TemplateView):
    template_name = 'success/stories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories'] = SuccessStory.objects.filter(is_published=True)
        context['featured_stories'] = SuccessStory.objects.filter(is_published=True)[:3]
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)[:4]
        return context


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
