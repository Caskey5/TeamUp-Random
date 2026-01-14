from django.views.generic import TemplateView

# Formation 5+1 Input View
class FirstFootballFormationInputView(TemplateView):
    template_name = "pages/input_pages/football_input/first_football_formation_input.html"

# Formation 4+1 Input View
class SecondFootballFormationInputView(TemplateView):
    template_name = "pages/input_pages/football_input/second_football_formation_input.html"

# Formation 10+1 Input View
class ThirdFootballFormationInputView(TemplateView):
    template_name = "pages/input_pages/football_input/third_football_formation_input.html"