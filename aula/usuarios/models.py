from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from musica.models import Song
from imagenes.models import Image


# Create your models here.
class Usersys(models.Model):
    TODAY = timezone.now().date()
    name = models.CharField(max_length=50)
    last_names = models.CharField(max_length=100)
    date_added = models.DateField('Fecha de alta', default=TODAY)
    songs = models.ManyToManyField(Song, default=None)
    images = models.ManyToManyField(Image, default=None)

    def __str__(self):
        return self.name
