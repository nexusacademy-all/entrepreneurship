from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestimonialViewSet, SuccessStoryViewSet

router = DefaultRouter()
router.register(r'testimonials', TestimonialViewSet)
router.register(r'stories', SuccessStoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
