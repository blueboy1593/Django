# pages/views
from django.shortcuts import render
from datetime import datetime
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


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Lift is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list=[]
    context = {
        'menus' : menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request, birthday):
    my_birthday = birthday
    context = {
        'my_birthday' : my_birthday,
    }

    return render(request, 'isitbirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lotto = sorted(random.sample(range(1,46), 6))

    context = {
        'real_lotto' : real_lotto,
        'lotto' : lotto,
    }
    
    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')


def result(request):
    category = request.GET.get('category')
    query = request.GET.get('query')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'result.html', context)


def lotto_pick(request):

    return render(request, 'lotto_pick.html')


def lotto_result(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    my_lotto = []
    for i in range(1,7):
        my_lotto.append(int(request.GET.get(f'num{i}')))
    my_lotto= sorted(my_lotto)
    context = {
        'real_lotto' : real_lotto,
        'my_lotto' : my_lotto,
    }
    return render(request, 'lotto_result.html', context)


def static_example(request):
    return render(request, 'static_example.html')


def practice(request):
    return render(request, 'practice.html')
