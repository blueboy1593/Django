from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# articles 의 메인 페이지, article list 를 보여 줌
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    # return redirect('index', context)
    return render(request, 'articles/index.html', context)

# Variable Routing 으로 사용자가 보기를 원하는 페이지 pk 를 받아서 Detail 페이지를 보여준다.
def detail(request, article_pk):
    # SELECT * FROM articles WHERE pk = 3 이런 느낌을 구현하는 것이다.
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    # return redirect('detail', context)
    return render(request, 'articles/detail.html', context)

# GET /articles/create/ 페이지만 받아가겠다 라는 경우.
# POST /articles/create/ 실제 작성하겟다????
# def new(request):
#     return render(request, 'articles/new.html')

# 데이터를 전달 받아서 article 생성
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title') # 데이터 따오기
        content = request.POST.get('content')
        article = Article()
        article.title = title
        article.content = content
        article.save()

        # return render(request, 'articles/create.html')
        # return redirect(f'/articles/{article.pk}/')
        return redirect('articles:detail', article.pk)

    # 만약 GET 요청으로 들어오면 html 페이지 rendering
    # 아니라면 (POST 일 경우) 사용자 데이터 받아서 article 생성
    # /articles/new/ 의 new.html 의 form 에서 전달받은 데이터들
    else:
        return render(request, 'articles/create.html')

# 사용자로부터 받은 article_pk 값에 해당하는 article을 삭제한다.
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)

def update(request, article_pk):
    # POST : 실제 Update 로직이 수행
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)

        title = request.POST.get('title')
        content = request.POST.get('content')

        article.title = title
        article.content = content
        article.save()
        return redirect('articles:index')

        
    # GET : Update 를 하기 위한 Form 을 제공하는 페이지
    else:
        article = get_object_or_404(Article, pk=article_pk)
        context = {'article': article}
        return render(request, 'articles/update.html', context)
    