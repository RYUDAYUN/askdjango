from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda numbers: int(numbers or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(requset, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))