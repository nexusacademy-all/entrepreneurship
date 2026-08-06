from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import TemplateView
from .models import Program, Registration, Workshop, Webinar
from .serializers import ProgramSerializer, RegistrationSerializer, WorkshopSerializer, WebinarSerializer


class ProgramListView(TemplateView):
    template_name = 'programs/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programs'] = Program.objects.filter(status='upcoming')
        context['featured_programs'] = Program.objects.filter(status='upcoming')[:3]
        return context


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'description']
    filterset_fields = ['type', 'status']


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['status', 'program']


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'description', 'instructor']
    filterset_fields = ['status']


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'description', 'speaker']
    filterset_fields = ['status']
