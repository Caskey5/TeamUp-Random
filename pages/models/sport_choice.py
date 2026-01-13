from django.db import models

class SportChoice(models.Model):
 
    SPORT_CHOICES = [
        ('football', 'Nogomet'),
        ('basketball', 'Košarka'),
        ('tennis', 'Tenis'),
        ('volleyball', 'Odbojka'),
        ('handball', 'Rukomet'),
    ]
    
    name = models.CharField(max_length=50, choices=SPORT_CHOICES, unique=True)
    display_name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sportovi'
        ordering = ['display_name']
    
    def __str__(self):
        return self.display_name
