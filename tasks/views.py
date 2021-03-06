from django.views.generic import TemplateView


class TasksListView(TemplateView):
    template_name = "tasks/list.html"
