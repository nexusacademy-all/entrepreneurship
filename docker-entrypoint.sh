#!/bin/bash
set -e

echo "Creating migrations..."
python backend/manage.py makemigrations users content framework programs community resources events success core --noinput --settings=backend.entrepreneurship.settings.production || true

echo "Running migrations..."
python backend/manage.py migrate --noinput --settings=backend.entrepreneurship.settings.production

echo "Collecting static files..."
python backend/manage.py collectstatic --noinput --settings=backend.entrepreneurship.settings.production || true

echo "Creating superuser..."
python backend/manage.py shell --settings=backend.entrepreneurship.settings.production << EOF
from users.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@nexusacademypro.com', 'admin123')
    print('Superuser created: admin / admin123')
else:
    print('Superuser already exists')
EOF

exec "$@"
