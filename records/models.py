from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubGenre(models.Model):
    name = models.CharField(max_length=100)
    main_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Release(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    first_released = models.DateTimeField
    genre = models.ManyToManyField(Genre)
    wanted = models.IntegerField(choices=list(zip(range(1, 5), range(1, 5))))
    in_collection = models.BooleanField(default=False)

    def __str__(self):
        return self.title


