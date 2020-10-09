from django.contrib import admin

from records.models import Artist, Release, SubGenre, Genre

admin.site.register(Artist)
admin.site.register(Release)
admin.site.register(Genre)
admin.site.register(SubGenre)