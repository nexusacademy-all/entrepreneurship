from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import TemplateView
from .models import Event
from .serializers import EventSerializer


class EventListView(TemplateView):
    template_name = 'events/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(status='upcoming')[:6]
        context['past_events'] = Event.objects.filter(status='completed')[:3]
        return context


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'description', 'location']
    filterset_fields = ['type', 'status']
