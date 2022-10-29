from asyncio.windows_events import NULL
from datetime import datetime
from email.policy import default
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)
    age = models.IntegerField(default = None)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length = 500)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    Content = models.CharField(max_length = 3000)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
   
    def __str__(self):
        return self.Content
