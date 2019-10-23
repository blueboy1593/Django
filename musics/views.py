from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import MusicSerializer, ArtistSerializer, CommentSerializer, ArtistDetailSerializer
# Create your views here.


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True) # 여러개를 쓰고 싶으면 many에 True를 주면 된다.
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)


@api_view(['GET'])
def artist_list(request):
    artist = Artist.objects.all()
    serializer = ArtistSerializer(artist, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)