from django.shortcuts import render, redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm

# 모든 article 을 보여주는 페이지
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# GET 으로 들어오면 생성하는 페이지 rendering
# POST 로 들어오면 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 사용자가 입력한 form이 유효한지를 검증하는 것. 그리고 유효한 경우에만 form을 받아서 가공을 합시다.
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        # valid하지 않은 이상한 값의 form을 넘겨줘버린다.
        # 이유는 ... 이상한 값일때 다시 다 타이핑하면 귀찮으니깐.
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)
    # Get 요청으로 들어왔을 때에는 이렇게 한다고 하는 것이다.
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)
# 내용을 줄어주는 과정.

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)