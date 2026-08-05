from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, ArticleViewSet, VideoViewSet, DownloadViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'downloads', DownloadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
