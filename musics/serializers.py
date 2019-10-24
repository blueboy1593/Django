from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)


class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(many=True)
    musics_count = serializers.IntegerField(source='musics.count')   # 음악 몇개 가지고 있는지 카운트 해주는 기능.

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count',) # count는 약간 내장함수같은 느낌.
        # 이런식으로 표기할 수가 있구나


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'music_id', 'content',)