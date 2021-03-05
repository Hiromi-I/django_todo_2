from django.contrib.auth.views import LoginView as _LoginView
from django.views.generic import TemplateView


class LoginView(_LoginView):
    template_name = 'accounts/login.html'


class HomeViw(TemplateView):
    template_name = 'accounts/home.html'
