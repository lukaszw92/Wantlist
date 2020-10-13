from django.shortcuts import render

def artistList(request):
    return render(request, 'frontend/artist_list.html')