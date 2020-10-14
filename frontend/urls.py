from django.urls import path
from frontend import views

urlpatterns = [
    path('artist_list/', views.artistList, name='artist_list'),
    ]