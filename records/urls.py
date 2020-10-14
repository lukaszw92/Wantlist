from django.urls import path
from records import views


urlpatterns = [
    path('', views.apiOverviewView.as_view()),

    path('artist_list/', views.ArtistsListView.as_view(), name='artist_list'),
    path('artist_detail/<str:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist_create/', views.ArtistCreateView.as_view(), name='artist_create'),
    path('artist_update/<str:pk>/', views.ArtistUpdateView.as_view(), name='artist_update'),
    path('artist_delete/<str:pk>/', views.ArtistDeleteView.as_view(), name='artist_delete'),

    path('genre_list/', views.GenreListView.as_view(), name='genre_list'),
    path('genre_detail/<str:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genre_create/', views.GenreCreateView.as_view(), name='genre_create'),
    path('genre_update/<str:pk>/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genre_delete/<str:pk>/', views.GenreDeleteView.as_view(), name='genre_delete'),

]