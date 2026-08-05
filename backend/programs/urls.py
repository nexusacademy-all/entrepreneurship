from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, RegistrationViewSet, WorkshopViewSet, WebinarViewSet

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'workshops', WorkshopViewSet)
router.register(r'webinars', WebinarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
