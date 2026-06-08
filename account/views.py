from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, TemplateView, View

from account.forms import LoginForm, SignUpForm
from pages.models import TeamGeneration


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:history')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:history')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Račun je kreiran. Dobrodošao u TeamUp!')
        return response

    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        if next_url:
            return next_url
        return super().get_success_url()


class AccountLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        if next_url:
            return next_url
        return reverse('account:history')


class AccountLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('pages:home')

    def post(self, request):
        logout(request)
        return redirect('pages:home')


class HistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'account/history.html'
    login_url = reverse_lazy('account:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generations'] = (
            TeamGeneration.objects.filter(
                user=self.request.user,
                is_saved=True,
            )
            .select_related('formation__sport')
            .prefetch_related('teams__players')
            .order_by('-saved_at')
        )
        return context


class SavedGenerationDetailView(LoginRequiredMixin, DetailView):
    model = TeamGeneration
    template_name = 'account/saved_generation_detail.html'
    context_object_name = 'generation'
    login_url = reverse_lazy('account:login')

    def get_queryset(self):
        return (
            TeamGeneration.objects.filter(
                user=self.request.user,
                is_saved=True,
            )
            .select_related('formation__sport')
            .prefetch_related('teams__players')
        )


class SaveGenerationView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            login_url = reverse('account:login')
            save_url = reverse('account:save_generation', kwargs={'pk': pk})
            return redirect(f'{login_url}?next={save_url}')

        generation = get_object_or_404(TeamGeneration, pk=pk)

        if generation.is_saved:
            if generation.user_id == request.user.id:
                messages.info(request, 'Ovaj rezultat je već spremljen u tvojoj povijesti.')
                return redirect('account:history')
            messages.error(request, 'Ovaj rezultat je već spremljen.')
            return redirect('pages:team_results', pk=generation.pk)

        generation.user = request.user
        generation.is_saved = True
        generation.saved_at = timezone.now()
        generation.save(update_fields=['user', 'is_saved', 'saved_at'])
        messages.success(request, 'Rezultati su spremljeni u tvoj račun!')
        return redirect('account:history')
