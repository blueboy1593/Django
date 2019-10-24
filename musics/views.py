from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music, Artist, Comment
from .serializers import MusicSerializer, ArtistSerializer, CommentSerializer, ArtistDetailSerializer
# Create your views here.


@api_view(['GET'])
def music_list(request):
    # 만약에 artist_pk 가 Query Params 로 넘어온다면, artist_pk 로 필터링 한 값만 응답한다.
    # 그렇지 않으면 전체 음악을 응답한다.
    params = {}
    artist_pk = request.GET.get('artist_pk')

    if artist_pk is not None:
        params['artist_id'] = artist_pk # artist_id는 내장함수처럼 되는건가보다..... 뭐 이런게 다있어.
        # 이건 복습 해야할 수 있음.

    musics = Music.objects.filter(**params)
    # musics = Music.objects.all()
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


# Postman을 통해서 포스트로 보내는 법을 알 수 있다아!
@api_view(['POST'])
def comments_create(request, music_pk):
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   # 검증에 실패하면 400 Bad Request 오류를 발생
        serializer.save(music_id=music_pk)  # 에러가 난다는 것은 코드 오류가 있다는 것...?
    return Response(serializer.data)    # 사용자가 방금 작성한 데이터를 보여주겠다
    

@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "PUT":
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  # 이러면 시리얼라이저의 데이터를 보여주고
    else:   # ==> 'DELETE'
        comment.delete()
        return Response({'message':'Comment has been deleted!'})    # 이러면 메세지가 출력되는 거구


@api_view(['PUT', 'DELETE'])
def music_updel(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)   # 얘는 어떤 짓을 하던 동일하게 사용할 코드이다.
    if request.method == "PUT":
        serializer = MusicSerializer(data=request.data, instance=music)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  # 이러면 시리얼라이저의 데이터를 보여주고
    else:   # ==> 'DELETE'
        music.delete()
        return Response({'message':'Music has been deleted!'})    # 이러면 메세지가 출력되는 거구