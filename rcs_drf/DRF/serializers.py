from rest_framework import serializers
#from rcs_drf.DRF.models import Album, Artist, Track
from .models import Album, Artist, Track
#from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
#from django.contrib.auth.models import User



class TrackSeializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name')

class ArtistSeializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name')

class AlbumSeializer(serializers.ModelSerializer):
    tracks = TrackSeializer(many=True, read_only=True)
    artist = ArtistSeializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('name', 'year', 'artist', 'tracks')

# def encode():
#     #Artist("Eminem")
#     #Album("Kamicadze", "Eminem", 2012)
#     #Track("My Band", "Kamicadze")
#     art = Artist(name='Pink Floyd')
#     alb = Album(name='The wall', artist=art, year=1999)
#     trc = Track(name="ComfortableNumb", album=alb)
#
#     print(Artist, Album, Track)
#     print("2")
#     print(Artist.__dict__, Album.__dict__, Track.__dict__, sep='\n')
#     print()
#     print(art.__dict__, alb.__dict__, trc.__dict__, sep='\n')
#
#     Artist_sr = ArtistSeializer()
#     print("++++++")
#     print(Artist_sr.data)
#     print("++++++")

#python manage.py shell
#from DRF.serializers import encode
#encode()
#quit()
