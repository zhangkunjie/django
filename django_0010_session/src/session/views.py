from _ast import Str
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'login.html')
def login(request):
    username= request.POST['username']
    password= request.POST['password']
    print("###########"+username)
    print("###########"+password)
    request.session["username"]=username
    request.session["password"]=password
    list=[1,2,3,4,5]
    request.session["list"]=list
    return render(request,"success.html")
