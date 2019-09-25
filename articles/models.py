from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() # 문자열의 빈 값 저장은 null이 아니라 ''이기 때문에 null=True는 적합하지 않다.
    
    # blank: 데이터 유효성과 관련되어 있다. 유효성 검사
    # null: DB와 관련되어 있다.
    # '', Null 이런식으로 저장 가능.
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article이 삭제되면 Comment도 함께 삭제'
    # article.comment_set
    # related_name == 'Article instance 가 comment 를 역참조 할 수 있는 이름을 정의'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content