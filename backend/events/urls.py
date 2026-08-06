from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventListView

router = DefaultRouter()
router.register(r'', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TemplateView.as_view(template_name='events/list.html'), name='events-list'),
]
