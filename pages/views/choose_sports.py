from django.views.generic import  CreateView
from django.urls import reverse_lazy

from ..models import SportChoice


class ChooseSportView(CreateView):
    model = SportChoice
    template_name = "pages/choose_sports.html"
    fields = "__all__"

    success_url = reverse_lazy("pages:choose_sports")
