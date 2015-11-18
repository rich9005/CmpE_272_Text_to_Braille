"""storytest URL Configuration

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
from django.conf.urls import patterns, include , url
#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

urlpatterns = patterns('',
	url(r'^$','story.views3.home',name='home'),
	url(r'^next/$','story.views3.clickNext',name='clickNext'),
	url(r'^prev/$','story.views3.clickPrevious',name='clickPrevious'),
    url(r'^book/$','story.views3.clickBooks',name='clickBooks'),
    url(r'^nextPage/$','story.views3.clickNextBook',name='clickNext'),
    url(r'^prevPage/$','story.views3.clickPreviousBook',name='clickPrevious'),
    url(r'^news/$','story.views3.home',name='home'),
    
	)
