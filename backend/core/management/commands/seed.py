from django.core.management.base import BaseCommand
from framework.models import Step, Tool, Resource, Exercise
from programs.models import Program
from events.models import Event
from success.models import SuccessStory, Testimonial
from django.utils.text import slugify
from decimal import Decimal
from datetime import date, time, timedelta


class Command(BaseCommand):
    help = 'Seed initial data for the Entrepreneurship Platform'

    def handle(self, *args, **options):
        self.stdout.write('Seeding initial data...')

        self.seed_framework_steps()
        self.seed_programs()
        self.seed_events()
        self.seed_success_stories()
        self.seed_testimonials()

        self.stdout.write(self.style.SUCCESS('Initial data seeded successfully!'))

    def seed_framework_steps(self):
        if Step.objects.exists():
            self.stdout.write('Framework steps already exist, skipping...')
            return

        step_data = [
            (1, 'Discover Your Passion', 'Identify the problems that ignite your passion and align with your skills and values.'),
            (2, 'Generate Business Ideas', 'Brainstorm and refine multiple business ideas based on the problems you have identified.'),
            (3, 'Validate Your Idea', 'Test your assumptions and validate that there is a real market need for your solution.'),
            (4, 'Define Your Value Proposition', 'Craft a clear, compelling value proposition that differentiates your offering.'),
            (5, 'Build Your MVP', 'Develop a minimum viable product to test with real users and gather feedback.'),
            (6, 'Assemble Your Team', 'Recruit the right co-founders and early team members with complementary skills.'),
            (7, 'Develop Your Business Model', 'Create a sustainable business model using frameworks like the Business Model Canvas.'),
            (8, 'Prepare for Market Entry', 'Plan your go-to-market strategy and prepare for a successful product launch.'),
            (9, 'Scale Your Operations', 'Optimize processes and systems to support growth without sacrificing quality.'),
            (10, 'Secure Funding', 'Understand different funding options and prepare for investor pitches.'),
            (11, 'Build Your Brand', 'Develop a strong brand identity and establish your presence in the market.'),
            (12, 'Master Sales & Marketing', 'Implement effective sales strategies and marketing campaigns to acquire customers.'),
            (13, 'Achieve Product-Market Fit', 'Iterate on your product until you achieve strong product-market fit.'),
            (14, 'Scale to New Markets', 'Expand into new markets and verticals while maintaining operational excellence.'),
        ]

        for step_number, title, description in step_data:
            Step.objects.get_or_create(
                step_number=step_number,
                defaults={
                    'title': title,
                    'slug': slugify(title),
                    'description': description,
                    'content': f'<p>This is the content for {title}. Detailed content will be added here.</p>',
                    'is_published': True,
                }
            )

        self.stdout.write(f'Created {len(step_data)} framework steps.')

    def seed_programs(self):
        if Program.objects.exists():
            self.stdout.write('Programs already exist, skipping...')
            return

        program_data = [
            {
                'title': 'Nexus Accelerator',
                'description': 'An intensive 12-week accelerator designed for early-stage startups ready to scale. Get mentorship, funding access, and expert guidance.',
                'type': 'accelerator',
                'start_date': date(2026, 9, 1),
                'end_date': date(2026, 11, 24),
                'price': Decimal('5000.00'),
                'capacity': 20,
                'status': 'upcoming',
            },
            {
                'title': 'Ideation Incubator',
                'description': 'A 8-week program for aspiring entrepreneurs with a business idea. Learn validation, MVP development, and pitch preparation.',
                'type': 'incubator',
                'start_date': date(2026, 10, 15),
                'end_date': date(2026, 12, 10),
                'price': Decimal('2500.00'),
                'capacity': 30,
                'status': 'upcoming',
            },
            {
                'title': 'Growth Bootcamp',
                'description': 'A 6-week intensive training program focused on scaling strategies, marketing funnels, and operational excellence.',
                'type': 'training',
                'start_date': date(2026, 11, 1),
                'end_date': date(2026, 12, 13),
                'price': Decimal('1500.00'),
                'capacity': 40,
                'status': 'upcoming',
            },
        ]

        for data in program_data:
            Program.objects.get_or_create(
                title=data['title'],
                defaults=data
            )

        self.stdout.write(f'Created {len(program_data)} programs.')

    def seed_events(self):
        if Event.objects.exists():
            self.stdout.write('Events already exist, skipping...')
            return

        event_data = [
            {
                'title': 'Entrepreneurship 101 Webinar',
                'description': 'An introductory webinar covering the fundamentals of starting a business. Perfect for first-time entrepreneurs.',
                'date': date(2026, 8, 20),
                'time': time(14, 0),
                'location': 'Online (Zoom)',
                'type': 'webinar',
                'price': Decimal('0.00'),
                'capacity': 500,
                'status': 'upcoming',
            },
            {
                'title': 'Startup Pitch Night',
                'description': 'An in-person event where entrepreneurs pitch their ideas to a panel of investors and industry experts.',
                'date': date(2026, 9, 5),
                'time': time(18, 0),
                'location': 'Nexus Academy Hall, Cairo',
                'type': 'meetup',
                'price': Decimal('50.00'),
                'capacity': 100,
                'status': 'upcoming',
            },
            {
                'title': 'Fundraising Workshop',
                'description': 'A hands-on workshop covering fundraising strategies, pitch deck creation, and investor relations.',
                'date': date(2026, 9, 15),
                'time': time(10, 0),
                'location': 'Online (Zoom)',
                'type': 'workshop',
                'price': Decimal('100.00'),
                'capacity': 50,
                'status': 'upcoming',
            },
        ]

        for data in event_data:
            Event.objects.get_or_create(
                title=data['title'],
                defaults=data
            )

        self.stdout.write(f'Created {len(event_data)} events.')

    def seed_success_stories(self):
        if SuccessStory.objects.exists():
            self.stdout.write('Success stories already exist, skipping...')
            return

        story_data = [
            {
                'title': 'From Idea to $1M Revenue in 18 Months',
                'excerpt': 'How Ahmed used the 14-step framework to validate his SaaS idea and achieve rapid growth.',
                'content': '<p>Ahmed started with just an idea...</p>',
                'author_name': 'Ahmed Hassan',
                'is_published': True,
            },
            {
                'title': 'Building a Sustainable Fashion Brand',
                'excerpt': 'Sarah transformed her passion for sustainable fashion into a thriving e-commerce business.',
                'content': '<p>Sarah always wanted to make a difference...</p>',
                'author_name': 'Sarah El-Masry',
                'is_published': True,
            },
            {
                'title': 'From Side Hustle to Full-Time Venture',
                'excerpt': 'Omar quit his corporate job after 6 months in the Nexus Accelerator program.',
                'content': '<p>Omar was working a 9-5 when he joined...</p>',
                'author_name': 'Omar Khaled',
                'is_published': True,
            },
        ]

        for data in story_data:
            SuccessStory.objects.get_or_create(
                title=data['title'],
                defaults=data
            )

        self.stdout.write(f'Created {len(story_data)} success stories.')

    def seed_testimonials(self):
        if Testimonial.objects.exists():
            self.stdout.write('Testimonials already exist, skipping...')
            return

        testimonial_data = [
            {
                'name': 'Nour Ali',
                'role': 'Founder, TechStart',
                'content': 'The 14-step framework gave me a clear path forward when I felt overwhelmed. Highly recommended!',
                'is_featured': True,
            },
            {
                'name': 'Karim Mansour',
                'role': 'CEO, GreenEnergy Co.',
                'content': 'The mentorship and community support were game-changers for my startup journey.',
                'is_featured': True,
            },
            {
                'name': 'Laila Fahmy',
                'role': 'Co-founder, EduTech',
                'content': 'I went from zero entrepreneurial knowledge to launching my own company in 6 months.',
                'is_featured': True,
            },
            {
                'name': 'Mostafa Ibrahim',
                'role': 'Founder, FinFlow',
                'content': 'The accelerator program was intense but incredibly valuable. Would do it again!',
                'is_featured': True,
            },
        ]

        for data in testimonial_data:
            Testimonial.objects.get_or_create(
                name=data['name'],
                role=data['role'],
                defaults=data
            )

        self.stdout.write(f'Created {len(testimonial_data)} testimonials.')
