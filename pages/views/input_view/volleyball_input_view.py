from pages.views.input_view.base_formation_input_view import BaseFormationInputView


class FirstVolleyballFormationInputView(BaseFormationInputView):
    formation_slug = 'volleyball_6v6'
    template_name = 'pages/input_pages/volleyball_input/first_volleyball_formation_input.html'


class SecondVolleyballFormationInputView(BaseFormationInputView):
    formation_slug = 'volleyball_4v4'
    template_name = 'pages/input_pages/volleyball_input/second_volleyball_formation_input.html'


class ThirdVolleyballFormationInputView(BaseFormationInputView):
    formation_slug = 'volleyball_2v2'
    template_name = 'pages/input_pages/volleyball_input/third_volleyball_formation_input.html'
