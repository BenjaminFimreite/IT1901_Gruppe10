from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Booking
from .models import Scene
from .models import Band


# Create your views here.
def create_booking(request):
	bookings = Booking.objects.all()
	template = loader.get_template('create_booking.html')
	context = {
        'bookings': bookings,
    }
	return HttpResponse(template.render(context, request))
