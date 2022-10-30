from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import AlbumSeializer, TrackSeializer, encode
from .models import Album, Track
from rest_framework.response import Response

class AlbumkView(APIView):
    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSeializer(album, many=True)
        #serializer = encode()
        print('*************************')
        print(serializer.data)
        return Response(serializer.data)

# class AlbumkView(APIView):
#     def get(self, request):
#         track = Track.objects.all()
#         serializer = TrackSeializer(track, many=True)
#         return Response(serializer.data)




# Create your views here.
