from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView

from .models import Artist, Release, Genre, SubGenre
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtistSerializer


class apiOverviewView(APIView):

    def get(self, request):
        urls = {
            "Artist List": "/artists/",
        }
        return Response(urls)


class ArtistsListView(APIView):

    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)


class ArtistDetailView(APIView):

    def get(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist, many=False)
        return Response(serializer.data)


class ArtistCreateView(APIView):

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class ArtistUpdateView(APIView):

    def put(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(instance=artist, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class ArtistDeleteView(APIView):

    def delete(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        artist.delete()

        return Response("Item deleted.")
