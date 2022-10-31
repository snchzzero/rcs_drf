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
        print('++++++++++++++++++++++++')
        for data in serializer_data:
            print(data)
            print()
            print(data['album'])
            print()
        return render(request, 'DRF/home.html', {'serializer_data': serializer_data})

    def post(self, request):
        album = Album.objects.all()
        serializer = AlbumSeializer(album, many=True)
        serializer_data = sorted(
            serializer.data, key=lambda k: k[request.data['sorted']], reverse=False)  # сортировка по полю
        #return Response({'post': serializer_data})  # для просмотра отправленного json запроса
        return render(request, 'DRF/home.html', {'serializer_data': serializer_data})


class NewArtistView(APIView):
    def get(self, request):
        return render(request, 'DRF/new_artist.html')

    def post(self, request):
        new_artist = Artist.objects.create(
            name=request.data['name']
        )
        #return Response({'post': NewArtistSeializer(new_artist).data})  # для просмотра отправленного json запроса

        message = "новый артист успешно добавлен"
        return render(request, 'DRF/new_artist.html', {'message': message})




class NewAlbumView(APIView):
    def get(self, request):
        CurrentArtists = Artist.objects.all()
        return render(request, 'DRF/new_album.html', {'CurrentArtists': CurrentArtists})

    def post(self, request):
        CurrentArtists = Artist.objects.all()
        serializer = NewAlbumSeializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ArtistId = ArtistID_to_Artists(request.data['artist'])
        if ArtistId:
            new_album = Album.objects.create(
                name=request.data['name'],
                artist=ArtistId,
                year=request.data['year']
            )
            #return Response({'post': NewAlbumSeializer(new_album).data})  # для просмотра отправленного json запроса
            message = "новый альбом успешно добавлен"
            return render(request, 'DRF/new_album.html', {'CurrentArtists': CurrentArtists, 'message': message})
        else:
            print('Ошибка ввода')
            print('Добавить страницу с ошибкой')

class NewTrackView(APIView):
    def get(self, request):
        CurrentAlbums = Album.objects.all()
        return render(request, 'DRF/new_track.html', {'CurrentAlbums': CurrentAlbums})

    def post(self, request):
        CurrentAlbums = Album.objects.all()
        serializer = TrackSeializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AlbumId = AlbumId_to_Albums(request.data['album'])
        if AlbumId:
            new_track = Track.objects.create(
                name=request.data['name'],
                album=AlbumId
            )
            #return Response({'post': TrackSeializer(new_track).data})  # для просмотра отправленного json запроса
            message = "новый трек успешно добавлен"
            return render(request, 'DRF/new_track.html', {'CurrentAlbums': CurrentAlbums, 'message': message})
        else:
            print('Ошибка ввода')
            print('Добавить страницу с ошибкой')

