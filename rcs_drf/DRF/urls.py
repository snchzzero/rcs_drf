from django.urls import path

from . import views

app_name = 'DRF'

urlpatterns = [
    path("album", views.AlbumView.as_view(), name='ShowAlbum'),
    path("new_artist", views.NewArtistView.as_view(), name='NewArtist'),
    path("new_album", views.NewAlbumView.as_view(), name='NewAlbum'),
    path("new_track", views.NewTrackView.as_view(), name='NewTrack'),
    path("sorted", views.AlbumView.as_view()),

    path("delete/track/<int:track_pk>", views.ShowTrackView, name='ShowTrack'),
    path("delete_track", views.DeleteTrack.as_view(), name='DeleteTrack'),

    path("delete/artist/<int:artist_pk>", views.ShowArtistView, name='ShowArtist'),
    path("delete_artist", views.DeleteArtist.as_view(), name='DeleteArtist'),

    path("delete/album/<int:album_pk>", views.ShowAlbumView, name='ShowAlbum'),
    path("delete_album", views.DeleteAlbum.as_view(), name='DeleteAlbum')
]