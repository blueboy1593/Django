from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    # nickname = forms.CharField()
    # content = forms.CharField()

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('content', 'nickname',)
        exclude = ['article', ]
        # 여기는 form으로 입력받을 데이터를 결정해주는 것이다.