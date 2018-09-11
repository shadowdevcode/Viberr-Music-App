from django.db import models
from django.urls import reverse


class Album(models.Model):
    album_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title + ' - ' + self.artist

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


