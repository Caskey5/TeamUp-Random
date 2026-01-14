from django.views.generic import TemplateView

# Formation 6+1 Input View
class FirstHandballFormationInputView(TemplateView):
    template_name = "pages/input_pages/handball_input/first_handball_formation_input.html"

# Formation 4+1 Input View
class SecondHandballFormationInputView(TemplateView):
    template_name = "pages/input_pages/handball_input/second_handball_formation_input.html"