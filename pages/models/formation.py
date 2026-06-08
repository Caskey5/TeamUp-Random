from django.db import models

from pages.models.sport_choice import SportChoice


class Formation(models.Model):
    slug = models.SlugField(max_length=80, unique=True)
    sport = models.ForeignKey(
        SportChoice,
        on_delete=models.CASCADE,
        related_name='formations',
    )
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)
    players_per_team = models.PositiveSmallIntegerField()
    has_goalkeeper = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    is_popular = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Formacija'
        verbose_name_plural = 'Formacije'
        ordering = ['sport', '-is_popular', 'players_per_team']

    def __str__(self):
        return f'{self.sport.display_name} - {self.display_name}'

    @property
    def sport_icon(self):
        icons = {
            'football': '⚽',
            'basketball': '🏀',
            'tennis': '🎾',
            'volleyball': '🏐',
            'handball': '🤾',
        }
        return icons.get(self.sport.name, '🏅')
