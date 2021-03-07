from django.urls import path
from .views import ListView, CreateView


app_name = "tasks"

urlpatterns = [
    path("list/", ListView.as_view(), name="list"),
    path("create/", CreateView.as_view(), name="create"),
]
