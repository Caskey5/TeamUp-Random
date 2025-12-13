from django.views.generic import TemplateView

# Index page
class IndexPageView(TemplateView):
    template_name = "index.html"
