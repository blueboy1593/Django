from django.shortcuts import render


def create(request):
    if request.method == 'POST':
        # Article 을 생성해달라고 하는 요청
        pass
    else: # GET
        # Article 을 생성하기 위한 페이지를 달라고 하는 요청
        # templates라는 폴더 안쪽에서 하는 것이 생략되어 있다고 생각하면 됨.
        return render(request, 'articles/create.html')
