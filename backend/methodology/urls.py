from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MethodologySectionViewSet, MethodologyView

router = DefaultRouter()
router.register(r'sections', MethodologySectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', MethodologyView.as_view(), name='methodology'),
]
