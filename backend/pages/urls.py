from django.urls import path
from .views import HomeView, MethodologyView, FrameworkOverviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('methodology/', MethodologyView.as_view(), name='methodology'),
    path('framework/', FrameworkOverviewView.as_view(), name='framework-overview'),
]
