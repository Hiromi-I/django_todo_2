from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = "tasks/list.html"


class CreateView(TemplateView):
    template_name = "tasks/create.html"
