# Django

## Django에서 주로 물어보는 개념

## 1. MTV

장고의 개발 방식은 MTV(Model, Template, View) 패턴을 따르며, 기본적으로 MVC와 많이 유사하다.

### Model

Class로 구현되며 데이터를 표현한다.

하나의 모델 클래스는 DB에서 하나의 테이블로 표현된다.

```python
class Post(models.Model):
    title = models.CharField(max=100)
    contents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save() 
```

위 모델에서 title, contents, create_date는 테이블의 필드가 된다.

각 필드는 models.CharField(), models.TextField()등 각 타입에 해당하는 클래스 객체를 생성해 할당한다.

즉, 필드는 인스턴스 변수가 아닌 클래스 변수로 생성한다.

### Template

HTML로 구현되며 화면에 보여주기위한 프리젠테이션 로직만을 가진다.

View에게 받은 데이터를 템플릿에 동적으로 적용한다.

일반적인 MVC패턴에서 View와 비슷한 역할

### View

메소드로 구현되며, HTTPRequest를 받아 HTTPResponse를 리턴하는 형태이다.

Model과 View를 중개하며, 비즈니스 로직의 핵심이다.(Model에서 받아온 데이터를 View로 전달)

일반적인 MVC패턴에서 Controller와 비슷한 역할



## 2. Serializer

### serializer.py

```python
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
```

### views.py - GET

```python
from rest_framework.decorators import api_view
@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
```

serializer는 간단하게 설명하면, queryset과 model instance 같은 것(쟝고로 모델링 하다보면 자연스레 생기는 것)을 'JSON'형태로 변환해주는 것이다.

### views.py - POST

```python
from rest_framework.decorators import api_view
# Postman을 통해서 포스트로 보내는 법을 알 수 있다!
@api_view(['POST'])
def comments_create(request, music_pk):
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   # 검증에 실패하면 400 Bad Request 오류를 발생
        serializer.save(music_id=music_pk)  # 에러가 난다는 것은 코드 오류가 있다는 것...?
    return Response(serializer.data)    # 사용자가 방금 작성한 데이터를 보여주겠다
```

이런식으로 POST로 온 데이터를 deserialize 하기도 한다.

api_view같은 decorator도 사용



## 3. SQLite

Django에서 우리가 주로 사용했던 데이터베이스

Mysql이나 PostgreSQL와 같은 데이터베이스 관리 시스템이지만, 서버가 아니라 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다.

Migration 과정을 거치면 db.sqlite3가 생기고 우리가 여기에 모델링해서 저장했음.



## Django 프로세스 했던 것들 여러가지

1. venv로 가상환경 설정

2. pip install로 Django 설치

3. 쟝고 프로젝트 시작

   ```bash
   $ django-admin startproject (프로젝트 이름)
   ```
   
4. 쟝고 앱 만들기

   ```bash
   $ python manage.py startapp (앱 이름)
   ```

5. 데이터 migrate 하기

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```

6. settings.py에 Third Party App 추가하기

   ```python
   INSTALLED_APPS = [
       # Local apps
       'articles',
       'accounts',
       'manytoone',
       'django_extensions',
   
       # Django apps
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

7. urls.py에서 app_name / urlpatterns 사용

   ```python
   app_name = 'accounts'
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('signup/', views.signup, name='signup'),
       path('login/', views.login, name='login')
   ]
   ```

8. models.py에서 유저 모델 정의(다른 곳에서는 영화, 코멘트 등)

   ```python
   from django.db import models
   from django.contrib.auth.models import AbstractUser
   from django.conf import settings
   
   class User(AbstractUser):
       followers = models.ManyToManyField(
           settings.AUTH_USER_MODEL,
           related_name='followings'
           )
   ```
