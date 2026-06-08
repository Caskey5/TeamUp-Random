from django.db import models

from pages.models.formation import Formation


class TeamGeneration(models.Model):
    formation = models.ForeignKey(
        Formation,
        on_delete=models.CASCADE,
        related_name='generations',
    )
    goalkeepers = models.JSONField(default=list, blank=True)
    field_players = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Generiranje timova'
        verbose_name_plural = 'Generiranja timova'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.formation} ({self.created_at:%d.%m.%Y %H:%M})'

    @property
    def total_players(self):
        return len(self.goalkeepers) + len(self.field_players)


class GeneratedTeam(models.Model):
    generation = models.ForeignKey(
        TeamGeneration,
        on_delete=models.CASCADE,
        related_name='teams',
    )
    name = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Tim'
        verbose_name_plural = 'Timovi'
        ordering = ['generation', 'order']

    def __str__(self):
        return self.name

    @property
    def player_count(self):
        return self.players.count()


class GeneratedPlayer(models.Model):
    team = models.ForeignKey(
        GeneratedTeam,
        on_delete=models.CASCADE,
        related_name='players',
    )
    name = models.CharField(max_length=100)
    is_goalkeeper = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Igrač'
        verbose_name_plural = 'Igrači'
        ordering = ['team', 'order']

    def __str__(self):
        return self.name
