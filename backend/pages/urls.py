from django.urls import path
from .views import HomeView, FrameworkOverviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('framework/', FrameworkOverviewView.as_view(), name='framework-overview'),
]
