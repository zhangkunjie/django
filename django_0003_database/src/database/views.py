"""
数据库的增删改查
"""
"""
保存1:直接保存   
"""

import json

from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render

from database.models import Student


def  save1(request):
  Student.objects.create(name="无邪",sex=1,age=26)
  return HttpResponse("操作成功！")
"""
保存2:直接保存   
"""
def  save2(request):
 student=Student(name="dream",sex=1,age=27) 
 student.save()
 return HttpResponse("操作成功！")
 """
保存3:设置属性然后保存   
"""
def  save3(request):
 student=Student()
 student.name="KK"
 student.sex=2
 student.age=25
 student.save()
 return HttpResponse("操作成功！")
 
"""
保存4:先查询如果没有再保存
"""
def  save4(request):
 student=Student.objects.get_or_create(id=10,name="dream",sex=1,age=27)
 return HttpResponse("操作成功！")
"""
更新12:先查询出来，改变属性，然后在save
"""
def update1(request):
    student=Student.objects.get(id=1)
    student.age=32
    student.save()
    return HttpResponse("操作成功！")   
"""
更新12:使用filter
"""
def update2(request):
    Student.objects.filter(id=1).update(age=22)
    return HttpResponse("操作成功！")   
"""
删除：delete
"""
def delete(request):
    Student.objects.filter(id=1).delete()
    return HttpResponse("操作成功！")  
"""
删除全部：deleteall
"""
def deleteAll(request):
    students=Student.objects.all()
    students.delete()
    return HttpResponse("操作成功！") 

"""
查询1：查询单个对象
"""
def select1(request):
    student=Student.objects.get(id=2)
    print(student.name)
    return HttpResponse("操作成功！") 
"""
查询2：使用filter
"""
def select2(request):
    """
        比较操作符= gt gte lt lte不能写>或者<
    """
    students=Student.objects.filter(id__gt=3)
    for s in students:
      print(s.name)
    return HttpResponse("操作成功！")
"""
查询3:查询全部
(1). 如果只是检查 Entry 中是否有对象，应该用 Entry.objects.all().exists()
(2). QuerySet 支持切片 Entry.objects.all()[:10] 取出10条，可以节省内存
(3). 用 len(es) 可以得到Entry的数量，但是推荐用 Entry.objects.count()来查询数量，后者用的是SQL：SELECT COUNT(*)
(4). list(es) 可以强行将 QuerySet 变成 列表
"""
def select3(request):
    #查询全部
    students=Student.objects.all()
    for s in students:
      print(s.name)
    return HttpResponse("操作成功！") 
"""
查询4：对查询结果排序
"""
def select4(request):
    students=Student.objects.filter(id__gt=3).order_by('age')
    for s in students:
      print(s.age)
    #返序 排列 
    students=Student.objects.filter(id__gt=3).order_by('age').reverse()
    for s in students:
      print(s.age)
    return HttpResponse("操作成功！")
"""
查询5：values和values_list
"""
def select5(request):
    #values:将查询结果封装成字典
    students=Student.objects.filter(id__gt=2).values("name")
    print(students)
    #values:将查询结果封装成列表
    students=Student.objects.filter(id__gt=2).values_list("name")
    print(students)
    return HttpResponse("操作成功！")
"""
查询5：返回数量
"""
def count(request):
    number=Student.objects.filter(id__gte=3).count()
    print(str(number))
    return HttpResponse("操作成功！")
"""
查询5：执行sql
"""
def raw(request):
    selectSQL=" select * from student s where id >3 "
    students = Student.objects.raw(selectSQL)  
    for s in students:
      print(s.name)
    return HttpResponse("操作成功！")

"""
查询5：直接执行sql语句
"""
def executeSQL(request):
    cursor = connection.cursor()
    #查询
    selectSQL=" select  * from student where id>3 "
    cursor.execute(selectSQL)
    #查询结果是一个元组列表
    students=cursor.fetchall()
    for s in students:
      print(s)
    #插入
    insertSQL=" insert into student values(15,'Tom',2,22) "  
    cursor.execute(insertSQL)
    #更新  
    updateSQL=" update student set age=18 where id=15 "  
    cursor.execute(updateSQL)
    #删除
    deleteSQL="delete from  student  where id=15 "  
    cursor.execute(deleteSQL)
    return HttpResponse("操作成功！")










def home(request):
    student=Student.objects.get(id=1)
    """
         字典中含有django.db.models.base.ModelState属性，不能构造json对象
    """
    print("###########"+str(student.__dict__))
    """
    to_JSON():去掉了django.db.models.base.ModelState属性，然后再构造json对象
    """
    sJson=student.to_JSON1()
    print("***********"+str(sJson))
    """
       或者也可以使用下面这种
    """
    #s_dict = model_to_dict(student)
    print("&&&&&&&&&&&&&&&&"+student.to_JSON2())
    """
         将json字符串转换成对象
    """
    s='{"sex": 1,"age": 23,"id": 1, "name": "\u6ce1\u6ce1"}'
    j = json.loads(s)
    stu = Student(**j)
    print(stu.name)
    return render(request, 'home.html',
                  {
                    'sjson':sJson
                   })
