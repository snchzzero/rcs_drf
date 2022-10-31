from rest_framework import serializers
from DRF.models import Album, Track, Artist
import rcs_drf.settings
#from .models import Album, Track, Artist

class NewArtistSeializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    class Meta:
        model = Album
        fields = ['album', 'name', 'artist']

class NewAlbumSeializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    class Meta:
        model = Album
        fields = ['name', 'artist', 'year']





class TrackSeializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    class Meta:
        model = Track
        #fields = '__all__'
        fields = ['album', 'name']


class AlbumSeializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    #track = TrackSeializer(many=True, read_only=True)
    tracks = serializers.StringRelatedField(many=True)

    #ser = Track.all()
    print('Тут должны быть треки:')
    #print(tracks, type(tracks), sep='\n')
    print('___________')
    #print(tracks.data)
    class Meta:
        model = Album
        fields = ['album', 'name', 'artist', 'tracks']
        #depth = 1
        #fields = '__all__'


def encode():

    album = Album.objects.all()
    for al in album:
        a = al.album
        print(a)
        print(Album.album(al))
        #b = al.name_y
        #print (b)
        print(al.name)
        print(al.year)
    serializer = AlbumSeializer(album, many=True)
    serializer2 = TrackSeializer(Track.objects.all(),  many=True)

    print(serializer.data)
    print("-------------------------------")
    print(serializer2.data)
    return serializer

encode()

#python manage.py shell
#from DRF.serializers import encode
#encode()
#quit()






