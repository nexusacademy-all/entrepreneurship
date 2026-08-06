from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import TemplateView
from .models import MethodologySection
from .serializers import MethodologySectionSerializer


class MethodologySectionViewSet(viewsets.ModelViewSet):
    queryset = MethodologySection.objects.filter(is_published=True)
    serializer_class = MethodologySectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'content']
    filterset_fields = ['section_type']


class MethodologyView(TemplateView):
    template_name = 'methodology/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = MethodologySection.objects.filter(is_published=True).order_by('order')
        return context
