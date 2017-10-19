from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^shifts$', views.shifts, name='shifts'),
    url(r'^bookings$', views.bookings, name="bookings"),
    url(r'^bookings/booking/(?P<booking_id>[0-9]+)/$', views.booking, name="booking"),
    url(r'^bookings/create_booking$', views.create_booking2, name="create_booking"),
    url(r'^bookings/pending_bookings$', views.pending_bookings, name="pending_bookings"),
    url(r'^send_email$', views.send_email, name="sendemail"),
    url(r'^bands$', views.bands, name="bands"),
    url(r'^bands/band/(?P<band_id>[0-9]+)/$', views.band, name="band"),
    url(r'^overview$', views.overview, name='overview'),
    url(r'^send_techneeds$', views.send_techneeds, name='send_techneeds'),
    url(r'^review_sent$', views.review_sent, name='review_sent'),
    url(r'^techneeds_sent$', views.techneeds_sent, name='techneeds_sent'),
    url(r'^booking_sent$', views.booking_sent, name='booking_sent'),
]
