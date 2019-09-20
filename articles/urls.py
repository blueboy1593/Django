from django.urls import path
from . import views

# /articles/ ___
app_name = 'articles'
urlpatterns = [
    # 입력 페이지 제공
    path('', views.index, name='index'),
    # /articles/10/ 이런식으로 몇번 게시글 보여주세요 라는 의미이다.
    path('<int:article_pk>/', views.detail, name='detail'), # detail
    # path('new/', views.new, name='new'),
    # create로 들어올 것이기 때문에 new의 url은 없애버렸다.
    path('create/', views.create, name='create'),
    # 4번째 article 삭제할 거
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
]
