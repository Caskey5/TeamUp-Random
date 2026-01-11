# ============================================
# models.py
# ============================================

from django.db import models
from django.contrib.auth.models import User


class Sport(models.Model):
    """Model za sportove"""
    SPORT_CHOICES = [
        ('football', 'Nogomet'),
        ('basketball', 'Košarka'),
        ('tennis', 'Tenis'),
        ('volleyball', 'Odbojka'),
        ('handball', 'Rukomet'),
    ]
    
    name = models.CharField(max_length=50, choices=SPORT_CHOICES, unique=True)
    display_name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='⚽')  # Emoji ikona
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sportovi'
        ordering = ['display_name']
    
    def __str__(self):
        return self.display_name


class Formation(models.Model):
    """Model za formacije/formate po sportu"""
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='formations')
    name = models.CharField(max_length=50)  # npr. "5+1", "6v6", "Pojedinačno"
    display_name = models.CharField(max_length=100)
    total_players = models.IntegerField()
    description = models.TextField()
    is_popular = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Formacija'
        verbose_name_plural = 'Formacije'
        ordering = ['sport', '-is_popular', 'total_players']
    
    def __str__(self):
        return f"{self.sport.display_name} - {self.display_name}"


class Team(models.Model):
    """Model za generirane timove"""
    name = models.CharField(max_length=100)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Tim'
        verbose_name_plural = 'Timovi'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.formation.sport.display_name}"


class Player(models.Model):
    """Model za igrače u timu"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, blank=True)  # npr. "Napadač", "Obrana"
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Igrač'
        verbose_name_plural = 'Igrači'
        ordering = ['team', 'order']
    
    def __str__(self):
        return f"{self.name} ({self.team.name})"


# ============================================
# forms.py
# ============================================

from django import forms
from .models import Sport, Formation


class SportChoiceForm(forms.Form):
    """Form za odabir sporta"""
    sport = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        label='Sport'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dinamički učitaj sportove iz baze
        sports = Sport.objects.all()
        self.fields['sport'].choices = [('', '-- Odaberi sport --')] + [
            (sport.name, f"{sport.icon} {sport.display_name}") 
            for sport in sports
        ]


class FormationChoiceForm(forms.Form):
    """Form za odabir formacije"""
    formation = forms.ModelChoiceField(
        queryset=Formation.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None,
        label='Formacija'
    )
    
    def __init__(self, sport_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if sport_name:
            sport = Sport.objects.get(name=sport_name)
            self.fields['formation'].queryset = Formation.objects.filter(sport=sport)


class TeamGenerationForm(forms.Form):
    """Form za generiranje timova"""
    team_name = forms.CharField(
        max_length=100,
        required=False,
        label='Ime tima (opcionalno)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'npr. Plavi tim'
        })
    )
    
    players = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 8,
            'placeholder': 'Unesi imena igrača (jedan po liniji):\nMarko\nAna\nIvan...'
        }),
        label='Igrači',
        help_text='Unesi ime svakog igrača u novi red'
    )
    
    def clean_players(self):
        """Validacija i čišćenje liste igrača"""
        players_text = self.cleaned_data['players']
        players = [p.strip() for p in players_text.split('\n') if p.strip()]
        
        if len(players) < 2:
            raise forms.ValidationError('Moraš unijeti barem 2 igrača!')
        
        # Provjeri duplikate
        if len(players) != len(set(players)):
            raise forms.ValidationError('Imaš duplikata u imenima igrača!')
        
        return players


# ============================================
# views.py
# ============================================

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
import random
from .models import Sport, Formation, Team, Player
from .forms import SportChoiceForm, FormationChoiceForm, TeamGenerationForm


def home(request):
    """Glavna stranica"""
    return render(request, 'base/home.html')


def choose_sport(request):
    """Stranica za odabir sporta"""
    if request.method == 'POST':
        form = SportChoiceForm(request.POST)
        if form.is_valid():
            sport_name = form.cleaned_data['sport']
            # Preusmjeri na stranicu za odabir formacije
            return redirect('sport_formations', sport_name=sport_name)
    else:
        form = SportChoiceForm()
    
    return render(request, 'pages/choose_sport.html', {'form': form})


def sport_formations(request, sport_name):
    """Stranica za odabir formacije ovisno o sportu"""
    sport = get_object_or_404(Sport, name=sport_name)
    formations = Formation.objects.filter(sport=sport)
    
    context = {
        'sport': sport,
        'formations': formations,
    }
    
    # Odaberi odgovarajući template ovisno o sportu
    templates = {
        'football': 'pages/football_formations.html',
        'basketball': 'pages/basketball_formats.html',
        'tennis': 'pages/tennis_formats.html',
        'volleyball': 'pages/volleyball_formats.html',
        'handball': 'pages/handball_formations.html',
    }
    
    template = templates.get(sport_name, 'pages/sport_formations.html')
    return render(request, template, context)


def generate_teams(request, formation_id):
    """Stranica za unos igrača i generiranje timova"""
    formation = get_object_or_404(Formation, id=formation_id)
    
    if request.method == 'POST':
        form = TeamGenerationForm(request.POST)
        if form.is_valid():
            players_list = form.cleaned_data['players']
            team_name = form.cleaned_data.get('team_name') or f"{formation.sport.display_name} Tim"
            
            # Provjeri da li ima dovoljno igrača
            if len(players_list) < formation.total_players:
                messages.warning(
                    request, 
                    f'Trebaš barem {formation.total_players} igrača za {formation.display_name}!'
                )
            else:
                # Generiraj timove
                teams = generate_random_teams(players_list, formation, team_name, request.user)
                return redirect('team_results', team_ids=','.join(str(t.id) for t in teams))
    else:
        form = TeamGenerationForm()
    
    context = {
        'form': form,
        'formation': formation,
    }
    return render(request, 'pages/generate_teams.html', context)


def team_results(request, team_ids):
    """Stranica sa rezultatima generiranih timova"""
    team_id_list = [int(id) for id in team_ids.split(',')]
    teams = Team.objects.filter(id__in=team_id_list).prefetch_related('players')
    
    context = {
        'teams': teams,
    }
    return render(request, 'pages/team_results.html', context)


# ============================================
# Helper Functions
# ============================================

def generate_random_teams(players_list, formation, base_team_name, user=None):
    """
    Generira nasumične timove od liste igrača
    """
    # Nasumično promiješaj igrače
    random.shuffle(players_list)
    
    teams = []
    players_per_team = formation.total_players
    num_teams = len(players_list) // players_per_team
    
    for i in range(num_teams):
        # Kreiraj tim
        team_name = f"{base_team_name} {i + 1}" if num_teams > 1 else base_team_name
        team = Team.objects.create(
            name=team_name,
            formation=formation,
            created_by=user if user and user.is_authenticated else None
        )
        
        # Dodaj igrače u tim
        start_idx = i * players_per_team
        end_idx = start_idx + players_per_team
        team_players = players_list[start_idx:end_idx]
        
        for order, player_name in enumerate(team_players, 1):
            Player.objects.create(
                team=team,
                name=player_name,
                order=order
            )
        
        teams.append(team)
    
    # Ako ima preostalih igrača
    remaining = len(players_list) % players_per_team
    if remaining > 0:
        # Možeš ovdje dodati logiku za pričuvne igrače ili kreiranje nepotpunog tima
        pass
    
    return teams


# ============================================
# urls.py
# ============================================

from django.urls import path
from . import views

urlpatterns = [
    # Glavna stranica
    path('', views.home, name='home'),
    
    # Odabir sporta
    path('choose-sport/', views.choose_sport, name='choose_sport'),
    
    # Formacije po sportu
    path('sport/<str:sport_name>/formations/', views.sport_formations, name='sport_formations'),
    
    # Generiranje timova
    path('formation/<int:formation_id>/generate/', views.generate_teams, name='generate_teams'),
    
    # Rezultati
    path('teams/<str:team_ids>/results/', views.team_results, name='team_results'),
]


# ============================================
# admin.py
# ============================================

from django.contrib import admin
from .models import Sport, Formation, Team, Player


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'icon', 'created_at']
    search_fields = ['display_name', 'name']


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['sport', 'display_name', 'total_players', 'is_popular']
    list_filter = ['sport', 'is_popular']
    search_fields = ['name', 'display_name']


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'formation', 'created_by', 'created_at']
    list_filter = ['formation__sport', 'created_at']
    search_fields = ['name']
    inlines = [PlayerInline]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'position', 'order']
    list_filter = ['team__formation__sport']
    search_fields = ['name', 'team__name']