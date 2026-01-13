from django.views.generic import TemplateView

class FootballFormatsView(TemplateView):
    template_name = "pages/formats_pages/football_formats.html"

class BasketballFormatsView(TemplateView):
    template_name = "pages/formats_pages/basketball_formats.html"

class TennisFormatsView(TemplateView):
    template_name = "pages/formats_pages/tennis_formats.html"

class HandballFormatsView(TemplateView):
    template_name = "pages/formats_pages/handball_formats.html"

class VolleyballFormatsView(TemplateView):
    template_name = "pages/formats_pages/volleyball_formats.html"
