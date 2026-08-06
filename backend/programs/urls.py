from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, RegistrationViewSet, WorkshopViewSet, WebinarViewSet, ProgramListView

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'workshops', WorkshopViewSet)
router.register(r'webinars', WebinarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', TemplateView.as_view(template_name='programs/list.html'), name='programs-list'),
]
