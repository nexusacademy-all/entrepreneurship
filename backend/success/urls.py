from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import TestimonialViewSet, SuccessStoryViewSet, SuccessStoryListView

router = DefaultRouter()
router.register(r'testimonials', TestimonialViewSet)
router.register(r'stories', SuccessStoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TemplateView.as_view(template_name='success/stories.html'), name='success-stories-list'),
]
