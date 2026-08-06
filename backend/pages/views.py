from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class MethodologyView(TemplateView):
    template_name = 'pages/methodology.html'


class FrameworkOverviewView(TemplateView):
    template_name = 'pages/framework_overview.html'
