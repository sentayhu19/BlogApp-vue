from django.views.generic.base import TemplateView # will render our template with ease
from django.contrib.auth.mixins import LoginRequiredMixin #Verifies that the current user is authenticated

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self): #overidden
        template_name = "index.html"
        return template_name