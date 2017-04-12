"""
页面静态化用的不是很多，因为当页面内容变了之后，静态化的内容不能随之改变
一般情况下啊都应该去使用缓存，因为缓存可以设置时间间隔定时同步
模板的相对路径问题还是没有解决，以后再说
"""
# Create your views here.

from _codecs import encode
import codecs
import os
import time

from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.template.response import TemplateResponse

from statichtml.models import Student


def  getStudentList(request):
  studentList= Student.objects.all()
  context = {'studentList': studentList}
  pwd = os.path.dirname(__file__)
  print("################"+pwd)
  static_html =pwd+'/static/html/student.html'
  static_html2 =pwd+'/static/html/t.html'
  print("***********"+str(static_html)) 
  if not os.path.exists(static_html):
    print("***********"+str(static_html)) 
    content = render_to_string('studentList.html', context)
    static_file=codecs.open(static_html, 'w','utf-8')
    #with open(static_html, 'w') as static_file:
    #        print(content)
    static_file.write(content)
  #return render_to_response(static_html)
  return render(request, static_html)