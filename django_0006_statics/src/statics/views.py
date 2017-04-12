from django.http.response import HttpResponse
from django.shortcuts import render
from _ast import Str


# Create your views here.
def index(request):
    return render(request, "index.html")
