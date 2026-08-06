from django.views.generic import TemplateView
from .models import AboutSection, Founder, TeamMember, TimelineEvent


class AboutView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = AboutSection.objects.filter(is_published=True).order_by('order')
        context['founder'] = Founder.objects.filter(is_active=True).first()
        context['team_members'] = TeamMember.objects.filter(is_active=True).order_by('order')
        context['timeline'] = TimelineEvent.objects.all().order_by('event_date', 'order')
        return context


class FounderView(TemplateView):
    template_name = 'about/founder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['founder'] = Founder.objects.filter(is_active=True).first()
        return context


class TimelineView(TemplateView):
    template_name = 'about/timeline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline'] = TimelineEvent.objects.all().order_by('event_date', 'order')
        return context


class TeamView(TemplateView):
    template_name = 'about/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.filter(is_active=True).order_by('order')
        return context
