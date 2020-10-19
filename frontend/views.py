from django.shortcuts import render

def main(request):
    return render(request, 'frontend/main.html')

def artistList(request):
    return render(request, 'frontend/artist_list.html')

def artistCreate(request):
    return render(request, 'frontend/artist_create.html')

def releaseList(request):
    return render(request, 'frontend/release_list.html')

def releaseCreate(request):
    return render(request, 'frontend/release_create.html')

