from django.contrib.auth.views import LoginView as _LoginView, LogoutView as _LogoutView
from django.views.generic import TemplateView


class LoginView(_LoginView):
    template_name = 'accounts/login.html'


class HomeView(TemplateView):
    template_name = 'accounts/home.html'


class LogoutView(_LogoutView):
    pass
