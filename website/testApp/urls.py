from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^hei/$', views.hei, name='hei'),
	url(r'^brann/$', views.brann, name='brann'),
]
