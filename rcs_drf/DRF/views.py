from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AlbumSeializer, TrackSeializer, NewAlbumSeializer, NewArtistSeializer
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


class AlbumView(APIView):
    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSeializer(album, many=True)
        serializer_data = serializer.data
        tracks = Track.objects.all()  # для привязки ссылки на трек
        artists = Artist.objects.all()
        albums = Album.objects.all()
        #return Response({'post': serializer_data})  # для просмотра отправленного json запроса
        return render(request, 'DRF/home.html', {'serializer_data': serializer_data, 'tracks': tracks,
                                                  'artists': artists, 'albums': albums})

    def post(self, request):
        album = Album.objects.all()

        serializer = AlbumSeializer(album, many=True)
        serializer_data = sorted(
            serializer.data, key=lambda k: k[request.data['sorted']], reverse=False)  # сортировка по полю
        #return Response({'post': serializer_data})  # для просмотра отправленного json запроса
        tracks = Track.objects.all()  # для привязки ссылки на трек
        artists = Artist.objects.all()
        albums = Album.objects.all()
        return render(request, 'DRF/home.html', {'serializer_data': serializer_data, 'tracks': tracks,
                                                 'artists': artists, 'albums': albums})


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
            Album.objects.create(
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
            Track.objects.create(
                name=request.data['name'],
                album=AlbumId
            )
            #return Response({'post': TrackSeializer(new_track).data})  # для просмотра отправленного json запроса
            message = "новый трек успешно добавлен"
            return render(request, 'DRF/new_track.html', {'CurrentAlbums': CurrentAlbums, 'message': message})
        else:
            print('Ошибка ввода')
            print('Добавить страницу с ошибкой')

def ShowTrackView(request, track_pk):
    track_name = Track.objects.get(id=track_pk)  # получить объект по id

    if request.method == 'GET':
        return render(request, 'DRF/delete_track.html', {'Track': track_name, 'track_pk': track_pk})

class DeleteTrack(APIView):
    def post(self, request):
        track = Track.objects.get(name=request.data['name'], id=request.data['id'])
        track.delete()
        message = "трек успешно удален"
        return render(request, 'DRF/delete_track.html', {'message': message})


def ShowArtistView(request, artist_pk):
    artist_name = Artist.objects.get(id=artist_pk)  # получить объект по id

    if request.method == 'GET':
        return render(request, 'DRF/delete_artist.html', {'Artist': artist_name})

class DeleteArtist(APIView):
    def post(self, request):
        artist = Artist.objects.get(name=request.data['name'])
        artist.delete()
        message = "артист успешно удален"
        return render(request, 'DRF/delete_artist.html', {'message': message})


def ShowAlbumView(request, album_pk):
    album_name = Album.objects.get(id=album_pk)  # получить объект по id

    if request.method == 'GET':
        return render(request, 'DRF/delete_album.html', {'Album': album_name})

class DeleteAlbum(APIView):
    def post(self, request):
        album = Album.objects.get(name=request.data['name'])
        album.delete()
        message = "альбом успешно удален"
        return render(request, 'DRF/delete_album.html', {'message': message})