from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)  # для связей Many to One
    year = models.IntegerField(blank=True,
                               validators=[MinValueValidator(1700), MaxValueValidator(2030)])

    def album(self):
        name_year_str = f'{self.name}[{self.year}]'
        return name_year_str

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE, null=True)  # для связей Many to One

    def __str__(self):
        return self.name

