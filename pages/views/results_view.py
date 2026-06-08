from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from pages.models import TeamGeneration
from pages.services import regenerate_teams


class TeamResultsView(View):
    template_name = 'pages/team_results/team_results.html'

    def get(self, request, pk):
        generation = get_object_or_404(
            TeamGeneration.objects.select_related('formation__sport').prefetch_related(
                'teams__players',
            ),
            pk=pk,
        )
        return render(request, self.template_name, {'generation': generation})

    def post(self, request, pk):
        generation = get_object_or_404(TeamGeneration, pk=pk)
        action = request.POST.get('action')

        if action == 'regenerate':
            regenerate_teams(generation)
            messages.success(request, 'Timovi su ponovno generirani!')

        return redirect('pages:team_results', pk=generation.pk)
