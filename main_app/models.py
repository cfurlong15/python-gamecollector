from django.db import models
from django.urls import reverse 

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length = 100)
    release_year = models.CharField(max_length = 4)
    rating = models.CharField(max_length = 4)
    genre = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})