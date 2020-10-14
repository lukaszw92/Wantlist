from rest_framework import serializers
from .models import Artist, Release, Genre, SubGenre

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = '__all__'


