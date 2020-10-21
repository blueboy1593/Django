from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.new, name='new'),
    # path('past_job/', views.result, name='result'),
]