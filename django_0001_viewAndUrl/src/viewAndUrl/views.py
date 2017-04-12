from django.http.response import HttpResponse
from django.shortcuts import render
from _ast import Str


# Create your views here.
def index(request):
    return HttpResponse(u"欢迎使用django!")
#加法运算1
def add1(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))
#加法运算2
def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))