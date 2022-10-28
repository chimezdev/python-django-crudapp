from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def artists(request):
    return render(request, 'artists.html')

def songs(request):
    return render(request, 'songs.html')