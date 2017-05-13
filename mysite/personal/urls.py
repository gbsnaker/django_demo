from django.conf.urls import url, include

from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'content/$', views.content, name='content')
]
