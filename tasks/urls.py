from django.urls import path
from .views import TasksListView, TasksCreateView


app_name = "tasks"

urlpatterns = [
    path("list/", TasksListView.as_view(), name="list"),
    path("create/", TasksCreateView.as_view(), name="create"),
]
