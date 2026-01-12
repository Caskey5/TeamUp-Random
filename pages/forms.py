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