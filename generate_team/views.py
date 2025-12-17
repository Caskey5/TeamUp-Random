from django.urls import reverse_lazy
from django.views.generic import  CreateView

from generate_team.models import SportChoice

# Create your views here.

class ChooseSportView(CreateView):
    model = SportChoice
    template_name = "pages/choose_sport.html"
    fields = "__all__"

    success_url = reverse_lazy("generate_team:choose_sport")