from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'landing/pre-register-home.html'