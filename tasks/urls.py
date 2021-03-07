from django.urls import path
from .views import ListView, CreateView, UpdateView, DeleteView


app_name = "tasks"

urlpatterns = [
    path("list/", ListView.as_view(), name="list"),
    path("create/", CreateView.as_view(), name="create"),
    path("update/", UpdateView.as_view(), name="update"),
    path("delete/", DeleteView.as_view(), name="delete"),
]
