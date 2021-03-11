from django.http.response import HttpResponse
from django.views.generic import (
    TemplateView,
    CreateView as _CreateView,
    ListView as _ListView,
)
from django.urls import reverse_lazy
from .forms import TaskCreationForm
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


class UpdateView(TemplateView):
    template_name = "tasks/update.html"


class DeleteView(TemplateView):
    template_name = "tasks/delete.html"


class DetailView(TemplateView):
    template_name = "tasks/detail.html"
