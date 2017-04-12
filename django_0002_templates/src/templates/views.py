import json

from django.shortcuts import render



def home(request):
    list=['java','c++','android','设计','产品经理']
    info_dict={'name':'张三','age':25,'city':'北京'}
    jsonStr1=['工人','农民','教师','学生']
    jsonStr2={'数学':98,'英语':'A','语文':80}
    return render(request, 'home.html',
                  {
                   'list':list,
                   'info_dict':info_dict,
                   'jsonStr1':json.dumps(jsonStr1),
                   'jsonStr2':json.dumps(jsonStr2),
                   })
