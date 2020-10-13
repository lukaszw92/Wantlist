from django.urls import path
from records import views

urlpatterns = [
    path('', views.apiOverviewView.as_view()),

    path('artists/', views.ArtistsListView.as_view(), name='artists'),
    path('artist/<str:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist_create/', views.ArtistCreateView.as_view(), name='artist_create'),
    path('artist_update/<str:pk>/', views.ArtistUpdateView.as_view(), name='artist_update'),
    path('artist_delete/<str:pk>/', views.ArtistDeleteView.as_view(), name='artist_delete'),

]