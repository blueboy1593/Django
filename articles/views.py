from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
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
            form.save()
            return redirect('articles:index')
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
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # 기존의 instance에 우리가 form으로 받은 데이터를 추가하는 것이다.
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else: # GET method
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form})


# @login_required
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        
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
        comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)
    # 인증되지 않았다는 내용