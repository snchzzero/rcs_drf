from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import AlbumSeializer, TrackSeializer, NewArtistSeializer, NewAlbumSeializer
from .models import Album, Track, Artist
from rest_framework.response import Response

def ArtistID_to_Artists(ArtistString):
    artists = Artist.objects.all()
    for artist in artists:
        if ArtistString == artist.name:
            ArtistId = artist
            return ArtistId
    return False

def AlbumId_to_Albums(album_chek):
    albums = Album.objects.all()
    for album in albums:
        if album_chek == album.name:
            AlbumId = album
            return AlbumId
    return False


class AlbumkView(APIView):
    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSeializer(album, many=True)
        #serializer = encode()
        print('*************************')
        print(serializer.data)

        serializer_data = sorted(
            serializer.data, key=lambda k: k['artist'], reverse=False)  # сортировка по полю
        #return Response(serializer_data)
        return render(request, 'DRF/home.html', {'serializer_data': serializer_data})

    def post(self, request):
        album = Album.objects.all()
        serializer = AlbumSeializer(album, many=True)
        serializer_data = sorted(
            serializer.data, key=lambda k: k[request.data['sorted']], reverse=False)  # сортировка по полю
        return Response({'post': serializer_data})

class NewArtistView(APIView):
    def post(self, request):
        new_artist = Artist.objects.create(
            name=request.data['artist']
        )
        return Response({'post': NewArtistSeializer(new_artist).data})

class NewAlbumView(APIView):

    def post(self, request):
        serializer = NewAlbumSeializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ArtistId = ArtistID_to_Artists(request.data['artist'])
        if ArtistId:
            new_album = Album.objects.create(
                name=request.data['name'],
                artist=ArtistId,
                year=request.data['year']
            )
            return Response({'post': NewAlbumSeializer(new_album).data})
        else:
            print('Ошибка ввода')
            print('Добавить страницу с ошибкой')

class NewTrackView(APIView):
    def post(self, request):
        serializer = TrackSeializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AlbumId = AlbumId_to_Albums(request.data['album'])
        if AlbumId:
            new_track = Track.objects.create(
                name=request.data['name'],
                album=AlbumId
            )
            return Response({'post': TrackSeializer(new_track).data})
        else:
            print('Ошибка ввода')
            print('Добавить страницу с ошибкой')

