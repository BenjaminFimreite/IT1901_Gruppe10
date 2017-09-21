from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^create_booking$', views.create_booking, name="create_booking"),
    #url(r'^create_booking$', TemplateView.as_view(template_name='create_booking.html'), name='create_booking'),
    url(r'^admin/', admin.site.urls),
    url(r'^create_booking$', TemplateView.as_view(template_name='create_booking.html'), name='create_booking'),
    url(r'^shifts$', TemplateView.as_view(template_name='shifts.html'), name='shifts'),
]
