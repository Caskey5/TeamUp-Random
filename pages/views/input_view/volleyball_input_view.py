from django.views.generic import TemplateView

# Formation 6v6 Input View
class FirstVolleyballFormationInputView(TemplateView):
    template_name = "pages/input_pages/volleyball_input/first_volleyball_formation_input.html"
    
# Formation 4v4 Input View
class SecondVolleyballFormationInputView(TemplateView):
    template_name = "pages/input_pages/volleyball_input/second_volleyball_formation_input.html"

# Formation 2v2 Input View
class ThirdVolleyballFormationInputView(TemplateView):
    template_name = "pages/input_pages/volleyball_input/third_volleyball_formation_input.html"