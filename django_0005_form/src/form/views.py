from django.http.response import HttpResponse
from django.shortcuts import render
from setuptools.command.build_ext import if_dl
from form.AddForm import AddForm

def index(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            sex=form.cleaned_data['sex']
            age=form.cleaned_data['age']
            email=form.cleaned_data['email']
            #print("姓名："+name+"性别："+str(sex)+"年龄："+str(age)+"e-mail:"+email)
            return  HttpResponse("姓名："+name+"性别："+str(sex)+"年龄："+str(age)+"e-mail:"+email)
    else:# 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
    