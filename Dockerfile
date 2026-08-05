FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p staticfiles media && \
    python manage.py collectstatic --noinput --settings=backend.entrepreneurship.settings.production || true

RUN chmod +x docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["gunicorn", "backend.entrepreneurship.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
