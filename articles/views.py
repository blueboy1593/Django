from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# from IPython import embed


@require_GET
def index(request):

    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


@require_GET
def detail(request, article_pk):
    # 사용자가 url 에 적어보낸 article_pk를 통해 디테일 페이지를 보여준다.
    # Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    comment_form = CommentForm()
    # form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        # Article 을 생성해달라고 하는 요청
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            # 이 부분은 자동으로 해주는 건지 자동함수같은 느낌인건지 정확하게 모르겠다
            article.save()
            return redirect('articles:detail', article.pk)
            # return redirect('articles:index')
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)
        # 데이터 꺼내서 Article 생성
        
    else: # GET
        # Article 을 생성하기 위한 페이지를 달라고 하는 요청
        # templates라는 폴더 안쪽에서 하는 것이 생략되어 있다고 생각하면 됨.
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 이렇게 해주는 이유는 update를 url을 통해서 들어와서 수정해버리려 할 수 있기 때문이다.
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
        # 기존의 instance에 우리가 form으로 받은 데이터를 추가하는 것이다.
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article_pk)
        else: # GET method
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article_pk)
    return render(request, 'articles/update.html', {'form': form})


# @login_required
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.user == request.user:
            article.delete()
        else:
            return redirect('articles:detail', article_pk)
    return redirect('articles:index')


@require_POST
def comments_create(request, article_pk):
    # article = get_object_or_404(Article, pk = article_pk)
    # if request.method == 'POST':
    if request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
        # 완전히 데이터베이스에 저장하지는 마라?? 임시로 빼놓으라는 것? 저장해버리면 안되서 그런가
            comment.article_id = article_pk
            comment.user = request.user
            comment.save()
        # 우리에게 필요한 데이터만 넣고 다시 저장한다 뭐 이런 뜻인가보다. 필요하지 않은 정보는??
        return redirect('articles:detail', article_pk)
    # 이렇게 되면 if 문 밖에서 유효하지 않을 때 알아서 다시 돌아가는 것이다.

    # 여기는 내가 한 부분이고 위에는 강사님이 알려주신 것이다.
    # if form.is_valid():
    #     comment = form.save(commit=False)
    #     comment.article_id = article_pk
    #     comment.save()
    #     return redirect('articles:detail', article_pk)
    # else:
    #     form = CommentForm()
    # context = {'form': form}
    # return render(request, 'articles/detail.html', context)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)
    # 인증되지 않았다는 내용


def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    # GET으로 가지고오면 없을 때 에러를 내기 때문에 filter를 사용하는 것이다.
    # 이 부분 헷갈리기 때문에...... 좀 다시볼 필요가 있다.
    if article.liked_users.filter(pk=user.pk).exists(): # 1개의 데이터라도 존재하면 True
        user.liked_articles.remove(article)
    else:
        user.liked_articles.add(article)
    return redirect('articles:detail', article_pk)


def follow(request, article_pk, user_pk):
    # 로그인한 유저가 게시글 유저를 Follow or Unfollow 한다.
    user = request.user # 로그인 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)

    if user in person.followers.all(): # 이미 팔로워임
        person.followers.remove(user) # 언팔하겠음
    else: # 팔로워가 아님
        person.followers.add(user) # 팔로우 하겠음

    return redirect('articles:detail', article_pk)