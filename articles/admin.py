from django.contrib import admin
from .models import Article
# 동일한 모델에 있는 아티클을 등록. admin이라는 미리 주어진 객체를 활용

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)

# Register your models here.
# admin.site.register(Article)
