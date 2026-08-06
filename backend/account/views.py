from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'auth/login.html'


class RegisterView(TemplateView):
    template_name = 'auth/register.html'


class ForgotPasswordView(TemplateView):
    template_name = 'auth/forgot_password.html'


class ResetPasswordView(TemplateView):
    template_name = 'auth/reset_password.html'
