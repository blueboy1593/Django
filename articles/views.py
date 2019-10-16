from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from .models import Article
from .forms import ArticleForm
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
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


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


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')