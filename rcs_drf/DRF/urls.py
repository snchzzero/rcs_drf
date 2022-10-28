from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet

router = DefaultRouter()
router.register('posts/', AlbumViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls))
]