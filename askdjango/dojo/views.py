import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda numbers: int(numbers or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(requset, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))


def post_list1(request):
    name='공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p> {name}  </p>
    <p> 여러분의 파이썬&장고의 페이스 메이커가 되어드리겠습니다. </p>
    '''.format(name=name))


def post_list2(request):
    name='공유'
    return render(request, 'dojo/post_list.html',{'name':name})


def post_list3(request):
    return JsonResponse({
        'message':'안녕 파이썬&장고',
        'items':['파이썬','장고','Celery','Azure','AWS'],
    },json_dumps_params={'ensure_ascii' : False})

def txt_download(request):
    #filepath='/Users/Ryudayun/dev/askdjango/test.txt'
    filepath = os.path.join(settings.BASE_DIR,'test.txt')
    filename=os.path.basename(filepath)
    with open(filepath,'rb') as f:
        response = HttpResponse(f, content_type='text/plain') #'text/html'
        response['Content-Disposition']='attachment; filename="{}"'.format(filename)
        return response 