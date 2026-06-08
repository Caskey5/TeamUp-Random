from pages.views.input_view.base_formation_input_view import BaseFormationInputView


class FirstHandballFormationInputView(BaseFormationInputView):
    formation_slug = 'handball_6_plus_1'
    template_name = 'pages/input_pages/handball_input/first_handball_formation_input.html'


class SecondHandballFormationInputView(BaseFormationInputView):
    formation_slug = 'handball_4_plus_1'
    template_name = 'pages/input_pages/handball_input/second_handball_formation_input.html'
