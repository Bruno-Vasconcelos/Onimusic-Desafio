from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Artist(models.Model):
    name = models.CharField(max_length=30)
    date_joined = models.DateField()

    def __str__(self):
        return self.name



class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    spotify_published = models.BooleanField()
    youtube_published = models.BooleanField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

