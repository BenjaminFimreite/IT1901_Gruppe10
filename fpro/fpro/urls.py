from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^create_booking$', views.create_booking2, name="create_booking"),
    url(r'^create_booking$', TemplateView.as_view(template_name='create_booking.html'), name='create_booking'),
    url(r'^admin/', admin.site.urls),
    url(r'^shifts$', views.shifts, name='shifts'),
	url(r'^view_bookings$', views.view_bookings, name="view_bookings"),
	url(r'^view_booking/(?P<booking_id>[0-9]+)/$', views.view_booking, name="view_booking"),
    url(r'^send_email$', views.send_email, name="sendemail"),
    url(r'^sentbooking$', TemplateView.as_view(template_name='sentbooking.html'), name="sentbooking"),
<<<<<<< HEAD
    url(r'^view_bands$', views.view_bands, name = "view_bands"),

=======
	url(r'^concert_overview$', views.concert_overview, name='concert_overview'),
>>>>>>> 6ebf241aa1810d275ad8a01d5aee3aeba043ba3e
]
