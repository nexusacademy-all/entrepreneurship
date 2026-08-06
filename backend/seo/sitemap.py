from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import AboutSection, MethodologySection
from framework.models import Step
from programs.models import Program
from events.models import Event
from success.models import SuccessStory


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['home', 'methodology', 'framework', 'programs', 'events', 'success', 'about', 'login', 'register']

    def location(self, item):
        return reverse(item)


class AboutSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return AboutSection.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class MethodologySitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return MethodologySection.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class FrameworkSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Step.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProgramSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return Program.objects.filter(status='upcoming')

    def lastmod(self, obj):
        return obj.updated_at


class EventSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return Event.objects.filter(status='upcoming')

    def lastmod(self, obj):
        return obj.updated_at


class SuccessStorySitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return SuccessStory.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
