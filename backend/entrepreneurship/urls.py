from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('core.urls')),
    path('auth/', include('account.urls')),
    path('', include('pages.urls')),
    path('methodology/', include('pages.urls')),
    path('framework/', include('pages.urls')),
    path('programs/', include('programs.urls')),
    path('events/', include('events.urls')),
    path('success/', include('success.urls')),
    path('api/users/', include('users.urls')),
    path('api/content/', include('content.urls')),
    path('api/framework/', include('framework.urls')),
    path('api/programs/', include('programs.urls')),
    path('api/community/', include('community.urls')),
    path('api/resources/', include('resources.urls')),
    path('api/events/', include('events.urls')),
    path('api/success/', include('success.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
