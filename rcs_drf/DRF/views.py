from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AlbumSeializer
from .models import Album
from rest_framework.response import Response

class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSeializer
    queryset = Album.objects.all()
    

# Create your views here.
