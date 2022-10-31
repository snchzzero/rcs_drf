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
    path("sorted", views.AlbumkView.as_view())
]