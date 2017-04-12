"""django_0003_database URL Configuration

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

from database import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^save1/$', views.save1),
    url(r'^save2/$', views.save2),
    url(r'^save3/$', views.save3),
    url(r'^save3/$', views.save3),
    url(r'^update1/$',views.update1),
    url(r'^update2/$', views.update2),
    url(r'^delete/$', views.delete),
    url(r'^deleteAll/$', views.deleteAll),
    url(r'^select1/$', views.select1),
    url(r'^select2/$', views.select2),
    url(r'^select3/$', views.select3),
    url(r'^select4/$', views.select4),
    url(r'^select5/$', views.select5), 
    url(r'^count/$', views.count),
    url(r'^raw/$', views.raw),
    url(r'^executeSQL/$', views.executeSQL),
    url(r'^$', views.home),
]
