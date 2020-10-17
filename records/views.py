from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView

from .models import Artist, Release, Genre, SubGenre
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtistSerializer, GenreSerializer, ReleaseSerializer

from rest_framework import generics


class apiOverviewView(APIView):

    def get(self, request):
        urls = {
            "Artist list": "/artist_list/",
            "Artist detail view": "/artist_detail/<str:pk>/",
            "Artist create view": "/artist_create/",
            "Artist update view": "/artist_update/<str:pk>/",
            "Artist delete view": "/artist_delete/<str:pk>/",

            "Genre list": "/genre_list/",
            "Genre detail view": "/genre_detail/<str:pk>/",
            "Genre create view": "/genre_create/",
            "Genre update view": "/genre_update/<str:pk>/",
            "Genre delete view": "/genre_delete/<str:pk>/",

            "Release list": "/release_list/",
            "Release create view": "/release_create/",
            "Release detail,update,delete ": "/release/<str:pk>/",

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

            if serializer.validated_data['surname'] == "":
                serializer.validated_data['surname'] = None

            try:
                Artist.objects.get(name=serializer.validated_data['name'],
                                   surname=serializer.validated_data['surname'])
            except Artist.DoesNotExist:
                serializer.save()

            else:
                raise Exception("Artist already exist")

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


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreUpdateView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDeleteView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReleaseListView(generics.ListAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ReleaseCreateView(generics.CreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ReleaseEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
