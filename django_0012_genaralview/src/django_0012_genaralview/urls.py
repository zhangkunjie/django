"""django_0012_genaralview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView, RedirectView
from genaralview.BiduRedirectView import BaiduRedirectView
from genaralview.StudentDetailView import StudentDetailView
from genaralview.StudentListView import StudentListlView
from genaralview.views import HomePageView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #这里使用的正则表达式进行url的匹配
    url(r'^about/', TemplateView.as_view(template_name="about.html"),name="about"),
    url(r'^home/', HomePageView.as_view(), name='home'),
    #自定义重定向
    url(r'^baidu/', BaiduRedirectView.as_view(), name='baidu'),
    #重定向
    url(r'^qq/', RedirectView.as_view(url='http://www.qq.com'), name='qq'),
    url(r'^studentdetail/(?P<pk>\d+)/$',StudentDetailView.as_view(), name='studentdetail'),
    url(r'^studentlist/', StudentListlView.as_view(), name='studentlist'),
]
