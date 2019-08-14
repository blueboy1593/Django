# pages/views
from django.shortcuts import render
import random

# 사용자가 보내는 요청에 대한 정보는 request에 있다.
def index(request): # 첫번째 인자는 반드시 request
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html') # render의 첫번째 인자도 반드시 request
    

def introduce(request):
    return render(request, 'introduce.html')

# Practice
# Variable routing 으로 'name'을 받아서 context에 'name'도 함께 넣는다.

def dinner(request, name):
    menu = ['강남 대창', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }

    return render(request, 'dinner.html', context)


def image(request):
    url = "https://picsum.photos/200"
    context = {
        'url': url,
    }
    return render(request, 'image.html', context)


# greeting/name/
def greeting(request, name):
    name = name
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    result=num1*num2
    context = {
        'result': result,
        'num1' : num1,
        'num2' : num2,
    }
    return render(request, 'times.html', context)








