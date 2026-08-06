from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import StepViewSet, ToolViewSet, ResourceViewSet, ExerciseViewSet, FrameworkOverviewView

router = DefaultRouter()
router.register(r'steps', StepViewSet)
router.register(r'tools', ToolViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'exercises', ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('overview/', TemplateView.as_view(template_name='framework/overview.html'), name='framework-overview'),
]
