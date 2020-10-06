from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class SubGenre(models.Model):
    name = models.CharField(max_length=100)
    main_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Release(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    first_released = models.DateTimeField
    genre = models.ManyToManyField(Genre)
    wanted = models.IntegerField(choices=list(zip(range(1, 5), range(1, 5))))
    in_collection = models.BooleanField(default=False)


