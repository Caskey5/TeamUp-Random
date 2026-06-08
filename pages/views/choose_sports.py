from django.views.generic import TemplateView


class ChooseSportView(TemplateView):
    template_name = 'pages/choose_sports.html'
