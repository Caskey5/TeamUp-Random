from django.views.generic import TemplateView


# Home page
class HomePageView(TemplateView):
    template_name = "base/home.html"
    
