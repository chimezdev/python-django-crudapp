from urllib import response
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#class based views
from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse, HttpResponse
#from rest_framework.parsers import JSONParser
#from django.views.decorators.csrf import csrf_exempt

class artisteView(APIView):
    def get(self, request):
        artistes = Artiste.objects.all()
        serialzer = ArtisteSerializer(artistes, many=True)
        return Response(serialzer.data)
    
    def post(self, request):
        serialzer = ArtisteSerializer(data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SongAPI(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serialzer = SongSerializer(songs, many=True)
        return Response(serialzer.data)
    
    def post(self, request):
        serialzer = SongSerializer(data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)



class LyricAPI(APIView):
    def get(self, request):
        lyrics = Lyric.objects.all()
        serialzer = LyricSerializer(lyrics, many=True)
        return Response(serialzer.data)
    
    def post(self, request):
        serialzer = LyricSerializer(data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
# function-based view
# @csrf_exempt
# def ArtisteView(request):
#     if request.method == 'GET':
#         artistes = Artiste.objects.all()
#         serialzer = ArtisteSerializer(artistes, many=True)
#         return JsonResponse(serialzer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serialzer = ArtisteSerializer(data=data)

#         if serialzer.is_valid():
#             serialzer.save()
#             return JsonResponse(serialzer.data, status=201)
#         return JsonResponse(serialzer.errors, status=400)

# def SongView(request):
#     if request.method == 'GET':
#         songs = Song.objects.all()
#         serialzer = SongSerializer(songs, many=True)
#         return JsonResponse(serialzer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serialzer = SongSerializer(data=data)

#         if serialzer.is_valid():
#             serialzer.save()
#             return JsonResponse(serialzer.data, status=201)
#         return JsonResponse(serialzer.errors, status=400)

# def LyricView(request):
#     if request.method == 'GET':
#         lyrics = Lyric.objects.all()
#         serialzer = LyricSerializer(lyrics, many=True)
#         return JsonResponse(serialzer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serialzer = LyricSerializer(data=data)

#         if serialzer.is_valid():
#             serialzer.save()
#             return JsonResponse(serialzer.data, status=201)
#         return JsonResponse(serialzer.errors, status=400)


class Artiste_detail(APIView):
    def get_object(self, pk):
        try:
            return Artiste.objects.get(id=pk)
        except Artiste.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        artiste = self.get_object(pk)
        serialzer = ArtisteSerializer(artiste)
        return Response(serialzer.data)
    
    def put(self, request, pk):
        artiste = self.get_object(pk)
        serialzer = ArtisteSerializer(artiste, data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        artiste = self.get_object(pk)
        artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class Song_detail(APIView):
    def get_object(self, pk): # a funct to get song using it id which is also its pk
        try:
            return Song.objects.get(id=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_object(pk) # calling the funct 'get_object'
        serialzer = SongSerializer(song)
        return Response(serialzer.data)
    
    def put(self, request, pk): #updating a song
        song = self.get_object(pk)
        serialzer = SongSerializer(song, data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk): # deleting a song
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class Lyric_detail(APIView):
    def get_object(self, pk):
        try:
            return Lyric.objects.get(id=pk)
        except Lyric.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        lyrics = self.get_object(pk)
        serialzer = LyricSerializer(lyrics)
        return Response(serialzer.data)
    
    def put(self, request, pk):
        lyrics = self.get_object(pk)
        serialzer = LyricSerializer(lyrics, data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lyrics = self.get_object(pk)
        lyrics.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# @csrf_exempt
# def artiste_detail(request, pk):
    
#     try:
#         artiste = Artiste.objects.get(id=pk)
#     except post.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serialzer = ArtisteSerializer(artiste)
#         return JsonResponse(serialzer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serialzer = ArtisteSerializer(artiste, data=data)
        
#         if serialzer.is_valid():
#             serialzer.save()
#             return JsonResponse(serialzer.data)
#         return JsonResponse(serialzer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         artiste.delete()
#         return HttpResponse(status=204)
    


# def index(request):
#     return render(request, 'index.html')

# def artists(request):
#     return render(request, 'artists.html')

# def songs(request):
#     return render(request, 'songs.html')