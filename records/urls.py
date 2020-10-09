from django.urls import path
from records import views

urlpatterns = [
    path('', views.apiOverviewView.as_view()),

    path('artists/', views.ArtistsListView.as_view()),
    path('artist_create/', views.ArtistCreateView.as_view())
    ]