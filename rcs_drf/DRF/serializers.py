from rest_framework import serializers
from DRF.models import Album, Track, Artist

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
        fields = ['album', 'name']


class AlbumSeializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album', 'name', 'artist', 'tracks']









