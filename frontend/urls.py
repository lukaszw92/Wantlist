from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.main, name='main'),
    path('artist_list/', views.artistList, name='artist_list'),
    path('artist_create/', views.artistCreate, name='artist_create'),
    path('release_list/', views.releaseList, name='release_list'),
    path('release_create/', views.releaseCreate, name='release_create'),
]