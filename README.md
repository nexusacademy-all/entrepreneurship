# Nexus Academy - Entrepreneurship Platform

A comprehensive Django-based platform for the Nexus Academy Entrepreneurship Program.

## Features

- 14-step entrepreneurship framework
- Content management (articles, videos, downloads)
- Programs and workshop registration
- Community forums and discussions
- Events and webinars
- Success stories and testimonials
- Resource library

## Tech Stack

- **Backend**: Django 4.2+, Django REST Framework
- **Frontend**: Tailwind CSS
- **Database**: PostgreSQL
- **Cache**: Redis
- **Task Queue**: Celery + Redis
- **Production**: Gunicorn, Nginx
- **Deployment**: Docker, Docker Compose

## Quick Start

```bash
# Clone repository
git clone <repo-url>
cd code

# Setup environment
cp .env.example .env
# Edit .env with your settings

# Start with Docker Compose
docker-compose up --build

# Or local development
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Docker Commands

```bash
docker-compose up -d
docker-compose down
docker-compose logs -f
docker-compose exec django_app python manage.py createsuperuser
```

## API Endpoints

- `/api/users/` - User management
- `/api/content/` - Articles, videos, downloads
- `/api/framework/` - Steps, tools, resources, exercises
- `/api/programs/` - Programs, registrations, workshops, webinars
- `/api/community/` - Forums, topics, posts, comments
- `/api/resources/` - Resource library
- `/api/events/` - Events
- `/api/success/` - Testimonials and success stories

## License

Copyright (c) Nexus Academy. All rights reserved.
