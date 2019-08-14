# pages/views
from django.shortcuts import render
import random

# 사용자가 보내는 요청에 대한 정보는 request에 있다.
def index(request): # 첫번째 인자는 반드시 request
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html') # render의 첫번째 인자도 반드시 request
    

def introduce(request):
    return render(request, 'introduce.html')


def dinner(request):
    menu = ['강남 대창', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }

    return render(request, 'dinner.html', context)
    