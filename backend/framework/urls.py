from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StepViewSet, ToolViewSet, ResourceViewSet, ExerciseViewSet

router = DefaultRouter()
router.register(r'steps', StepViewSet)
router.register(r'tools', ToolViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'exercises', ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
