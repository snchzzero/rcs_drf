from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import AlbumSeializer
from .models import Album
from rest_framework.response import Response

class AlbumkView(APIView):
    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSeializer(album, many=True)
        return Response(serializer.data)





# Create your views here.
