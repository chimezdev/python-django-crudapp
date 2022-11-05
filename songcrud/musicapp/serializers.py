from rest_framework import serializers
from .models import *

class ArtisteSerializer(serializers.ModelSerializer):
    
    # using SS means we have to do everythn manually
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age']
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['artiste_id', 'title', 'release_date', 'likes']
    
class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['song_id', 'content']
        
            