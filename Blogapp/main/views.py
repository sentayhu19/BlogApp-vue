from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class Index (LoginRequiredMixin,TemplateView):
    def get_template_names(self):
        template_name = "index.html"
        return template_name