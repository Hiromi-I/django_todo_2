from django.urls import path
from .views import ListView, CreateView, UpdateView, DeleteView, DetailView


app_name = "tasks"

urlpatterns = [
    path("list/", ListView.as_view(), name="list"),
    path("create/", CreateView.as_view(), name="create"),
    path("update/<int:pk>/", UpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", DetailView.as_view(), name="detail"),
]
