from rest_framework import serializers
from .models import Album, Track

class TrackSeializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    class Meta:
        model = Track
        fields = '__all__'



class AlbumSeializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field="name", read_only=True, many=False)
    track = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Album
        fields = ('name', 'artist', 'track')








