from django.db import models

# Create your models here.

class SportChoice(models.Model):
    SPORT_CHOICES = [
        ('soccer', 'Soccer'),
        ('basketball', 'Basketball'),
        ('baseball', 'Baseball'),
        ('hockey', 'Hockey'),
        ('volleyball', 'Volleyball'),
    ]

    sport = models.CharField(max_length=50, choices=SPORT_CHOICES)
    num_team_members = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.num_team_members} members"
    