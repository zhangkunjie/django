# coding=UTF-8
"""
第一种导入方法：使用get_or_create导入txt
"""
import os

from django.core import serializers
from django.core.serializers import get_serializer
from django.core.wsgi import get_wsgi_application
from importdata.models import Student
def import1():
    f=open("D://student.txt")
    for line in f:
        id,name,sex,age=line.split("\t")
        """
        get_or_create():避免重复导入出错
        """ 
        Student.objects.get_or_create(id=id,name=name,sex=sex,age=age)
    f.close()
"""
第二种导入方法：使用bulk_create,一次导入多条数据txt
注意：主键不能重复
"""
def import2():
    f=open("D://student.txt")
    studentList=[]
    for line in f:
        id,name,sex,age=line.split("\t")
        student=Student(id,name,sex,age)
        studentList.append(student)
    f.close()
    Student.objects.bulk_create(studentList) 
     
"""
第三种导入方法：使用反序列化
"""
def import3():
  #注意这里得设置环境变量  
  os.environ['DJANGO_SETTINGS_MODULE'] = 'importdata.settings'
  application = get_wsgi_application()   
  f=open("D:\\mymodel.json","r",encoding="utf-8-sig")
  for obj in serializers.deserialize("json",f):                     
    obj.save()
"""
导出方法1：导出文本
"""
def export1():
    out = open("D:\\student1.txt", "w",encoding="utf-8-sig")
    studentList=Student.objects.all()
    for s in studentList:
        out.write(str(s.id)+"\t"+s.name+"\t"+str(s.sex)+"\t"+str(s.age)+"\r\n")    
    out.close()    
"""
导出方法2：使用序列化
"""
def export2():
 data = serializers.serialize("json", Student.objects.all())
 out = open("D:\\mymodel.json", "w",encoding="utf-8-sig")
 out.write(data)
 out.close()
"""
其他导入导出导出方法：使用脚本
进入manage.py路径
1 导出：python manage.py dumpdata [appname] > appname_data.json
    例子：比如我们有一个项目叫 mysite, 里面有一个 app 叫 blog ,我们想导出 blog 的所有数据
  python manage.py dumpdata blog > blog_dump.json
2导入：python manage.py loaddata blog_dump.json
"""
import3()    
#export2()
"""
数据库联用
使用的时候和一个数据库的区别是:

如果不是defalut(默认数据库）要在命令后边加 --database=数据库对应的settings.py中的名称  如： --database=db1  或 --database=db2

数据库同步（创建表）
python manage.py syncdb #同步默认的数据库，和原来的没有区别
 
#同步数据库 db1 (注意：不是数据库名是db1,是settings.py中的那个db1，不过你可以使这两个名称相同，容易使用)
python manage.py syncdb --database=db1

数据导出
python manage.py dumpdata app1 --database=db1 > app1_fixture.json
python manage.py dumpdata app2 --database=db2 > app2_fixture.json
python manage.py dumpdata auth > auth_fixture.json

数据库导入
python manage.py loaddata app1_fixture.json --database=db1
python manage.py loaddata app2_fixture.json --database=db2

"""
