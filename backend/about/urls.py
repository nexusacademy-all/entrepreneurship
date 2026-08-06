from django.urls import path
from .views import AboutView, FounderView, TimelineView, TeamView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('founder/', FounderView.as_view(), name='founder'),
    path('timeline/', TimelineView.as_view(), name='timeline'),
    path('team/', TeamView.as_view(), name='team'),
]
