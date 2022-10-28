from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT, null=True)  # для связей Many to One
    year = models.IntegerField(blank=True,
                               validators=[MinValueValidator(1700), MaxValueValidator(2030)])
    name_year = f"{name}[{year}]"

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)  # для связей Many to One

    def __str__(self):
        return self.name

