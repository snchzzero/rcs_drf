from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'DRF'

# router = DefaultRouter()
# router.register('posts', TrackSeializer, basename='posts')
#
# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = [
    path("album", views.AlbumkView.as_view(), name='ShowAlbum'),
    path("new_artist", views.NewArtistView.as_view(), name='NewArtist'),
    path("new_album", views.NewAlbumView.as_view(), name='NewAlbum'),
    path("new_track", views.NewTrackView.as_view(), name='NewTrack'),
    path("sorted", views.AlbumkView.as_view()),

    path("delete/track/<int:track_pk>", views.ShowTrackView, name='ShowTrack'),
    path("delete_track", views.DeleteTrack.as_view(), name='DeleteTrack'),

    path("delete/artist/<int:artist_pk>", views.ShowArtistView, name='ShowArtist'),
    path("delete_artist", views.DeleteArtist.as_view(), name='DeleteArtist'),

    path("delete/album/<int:album_pk>", views.ShowAlbumView, name='ShowAlbum'),
    path("delete_album", views.DeleteAlbum.as_view(), name='DeleteAlbum'),



]