from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache


def health_check(request):
    try:
        connection.ensure_connection()
        cache.set('health_check', 'ok', 10)
        cache.get('health_check')
        return JsonResponse({'status': 'healthy', 'database': 'connected', 'cache': 'connected'})
    except Exception as e:
        return JsonResponse({'status': 'unhealthy', 'error': str(e)}, status=500)
