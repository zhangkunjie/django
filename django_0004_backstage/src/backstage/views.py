from django.shortcuts import render

# Create your views here.
"""
网站后台搭建步骤：
1新建django项目django_0004_backstage
2新建application:backstage
3修改django_0004_backstage下settings.py:
 在INSTALLED_APPS中增加元组，'backstage',
 修改数据库配置：
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test',                      # Or path to django_0003_database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}
4修改backstage下的_init_.py,添加pymysql支持:
  import pymysql
  pymysql.install_as_MySQLdb()
5修改models.py增加student模型...具体参照上一个项目的models
6修改backstage下的admin.py 文件 
  from django.contrib import admin
  from .models import Student
  admin.site.register(Student)
7选择项目-右键-Django
  先执行makemigrations
 再执行：migrate
8进入 manage.py所在文件夹：这里是
 D:\Program Files\workspace\python\django_0004_backstage\src
 注意：第7步也可以在这里执行：
 python manage.py makemigrations
 python manage.py migrate
 创建超级用户： 
  执行python manage.py createsuperuser添加超级用户
9启动项目，用刚才创建的账户登陆后台
"""