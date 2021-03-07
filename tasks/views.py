from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = "tasks/list.html"


class CreateView(TemplateView):
    template_name = "tasks/create.html"


class UpdateView(TemplateView):
    template_name = "tasks/update.html"


class DeleteView(TemplateView):
    template_name = "tasks/delete.html"
