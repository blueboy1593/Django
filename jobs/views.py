from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
import requests
from pprint import pprint

fake = Faker()
url = 'http://api.giphy.com/v1/gifs/search?api_key=4i1aScgdTDrEGFZuIltFlaHACRS0QWA6&q='
url2 = '&limit=1'

def new(request):
    if request.method == 'POST':
        name = request.POST.get('name') # 데이터 따오기
        # 데이터베이스에 name으로 저장된 전생직업 있는지 확인
        # 있다면 보여주고 없다면 새로 만들어서 저장
        # person = Job.objects.filter(name=name).first()
        # if person:
        #     context = {'person': person}
        # else:
        job = Job()
        job.name = name
        job.past_job = fake.job()
        job.save()
        new_url = url + job.past_job + url2
        data1 = requests.get(new_url).json()
        data = data1['data'][0]['images']['downsized']['url']
        context = {'data': data,
                'jobbb': job,
        }
        return render(request, 'jobs/result.html', context)

    else:
        return render(request, 'jobs/input.html')

# def result(request):
#     # jobs = Job.objects.all()
#     context = {'data': data}
#     return render(request, 'jobs/result.html', context)