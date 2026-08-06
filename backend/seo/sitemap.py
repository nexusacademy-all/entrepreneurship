from django.contrib.sitemaps import Sitemap
from django.urls import reverse


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
        from about.models import AboutSection
        return AboutSection.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class MethodologySitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        from methodology.models import MethodologySection
        return MethodologySection.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class FrameworkSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        from framework.models import Step
        return Step.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProgramSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        from programs.models import Program
        return Program.objects.filter(status='upcoming')

    def lastmod(self, obj):
        return obj.updated_at


class EventSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        from events.models import Event
        return Event.objects.filter(status='upcoming')

    def lastmod(self, obj):
        return obj.updated_at


class SuccessStorySitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        from success.models import SuccessStory
        return SuccessStory.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
