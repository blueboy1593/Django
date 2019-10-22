from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.conf import settings

# article.user
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 한명의 user가 계속 article을 낼 건데 그러기 때문에 속하는 것일 것!!!)

    class Meta:
        ordering = ('-pk', )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    nickname = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content


class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=100,
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
        )
    age = models.IntegerField(
        validators=[MinValueValidator(19, message="미성년자는 노노에요")]
    )

class Musician(models.Model):
    # PK = models.IntegerField()
    FIRST_NAME = models.CharField(max_length=20)
    LAST_NAME = models.CharField(max_length=20)