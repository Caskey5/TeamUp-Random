from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from pages.models import Formation
from pages.services import create_team_generation


class BaseFormationInputView(View):
    formation_slug = ''
    template_name = ''

    def get(self, request):
        formation = get_object_or_404(Formation, slug=self.formation_slug)
        return render(request, self.template_name, {'formation': formation})

    def post(self, request):
        formation = get_object_or_404(Formation, slug=self.formation_slug)
        try:
            generation = create_team_generation(formation, request.POST)
        except ValidationError as exc:
            messages.error(request, exc.messages[0])
            return render(request, self.template_name, {'formation': formation})

        return redirect('pages:team_results', pk=generation.pk)
