from django.views.generic import TemplateView

# Index page
class HomePageView(TemplateView):
    template_name = "base/home.html"
