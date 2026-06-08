from pages.views.input_view.base_formation_input_view import BaseFormationInputView


class FirstFootballFormationInputView(BaseFormationInputView):
    formation_slug = 'football_5_plus_1'
    template_name = 'pages/input_pages/football_input/first_football_formation_input.html'


class SecondFootballFormationInputView(BaseFormationInputView):
    formation_slug = 'football_4_plus_1'
    template_name = 'pages/input_pages/football_input/second_football_formation_input.html'


class ThirdFootballFormationInputView(BaseFormationInputView):
    formation_slug = 'football_10_plus_1'
    template_name = 'pages/input_pages/football_input/third_football_formation_input.html'
