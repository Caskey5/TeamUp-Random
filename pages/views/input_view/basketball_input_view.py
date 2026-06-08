from pages.views.input_view.base_formation_input_view import BaseFormationInputView


class FirstBasketballFormationInputView(BaseFormationInputView):
    formation_slug = 'basketball_6v6'
    template_name = 'pages/input_pages/basketball_input/first_basketball_formation_input.html'


class SecondBasketballFormationInputView(BaseFormationInputView):
    formation_slug = 'basketball_3v3'
    template_name = 'pages/input_pages/basketball_input/second_basketball_formation_input.html'
