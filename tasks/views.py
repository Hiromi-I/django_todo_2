from django.http.response import HttpResponse
from django.views.generic import (
    TemplateView,
    CreateView as _CreateView,
    ListView as _ListView,
    DetailView as _DetailView,
    UpdateView as _UpdateView,
    DeleteView as _DeleteView,
)
from django.urls import reverse_lazy, reverse
from .forms import TaskCreationForm, TaskUpdateForm
from .models import Task


class ListView(_ListView):
    template_name = "tasks/list.html"
    model = Task


class CreateView(_CreateView):
    template_name = "tasks/create.html"
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("tasks:list")

    def form_valid(self, form: TaskCreationForm) -> HttpResponse:
        form.instance.author = self.request.user
        form.instance.is_complete = False
        return super().form_valid(form)


class UpdateView(_UpdateView):
    template_name = "tasks/update.html"
    model = Task
    form_class = TaskUpdateForm

    def form_valid(self, form: TaskUpdateForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("tasks:detail", kwargs={"pk": self.object.pk})


class DeleteView(_DeleteView):
    template_name = "tasks/delete.html"
    model = Task
    success_url = reverse_lazy("tasks:list")


class DetailView(_DetailView):
    template_name = "tasks/detail.html"
    model = Task
