from django.urls import path
from .views import LoginView, HomeViw


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeViw.as_view(), name='home'),
]
