from pages.views.input_view.base_formation_input_view import BaseFormationInputView


class FirstTennisFormationInputView(BaseFormationInputView):
    formation_slug = 'tennis_2v2'
    template_name = 'pages/input_pages/tennis_input/first_tennis_formation_input.html'
