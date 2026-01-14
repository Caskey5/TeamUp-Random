from django.views.generic import TemplateView

# Formation 6v6 Input View
class FirstBasketballFormationInputView(TemplateView):
    template_name = "pages/input_pages/basketball_input/first_basketball_formation_input.html"

# Formation 3v3 Input View
class SecondBasketballFormationInputView(TemplateView):
    template_name = "pages/input_pages/basketball_input/second_basketball_formation_input.html"
