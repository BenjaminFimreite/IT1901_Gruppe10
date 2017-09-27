from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import BandInfo
from django.template import RequestContext
from django.shortcuts import render_to_response

from .models import Booking
from .models import Scene
from .models import Band


# Create your views here.
def send_email(request):
	manager = request.POST.get('name')
	print(manager)
	comment = request.POST.get('comment')
	price = request.POST.get('price')
	msg = "Prisforslag: " + price + "\n" + "Kommentar: " + comment
	sender = 'fpro.no'
	subject = 'Bookingtilbud'
	if comment and manager:
		try:
			send_mail(subject, msg, sender, [manager])
		except BadHeaderError:
			return HttpResponse('Invalid header found')
		return HttpResponseRedirect('/sentbooking')
	else:
		return HttpResponse('Make sure all fields are entered and valid.')


def create_booking(request):
	bookings = Booking.objects.all()
	template = loader.get_template('create_booking.html')
	context = {
        'bookings': bookings,
    }
	return HttpResponse(template.render(context, request))

def shifts(request):
    template = loader.get_template('shifts.html')
    context = {}
    return HttpResponse(template.render(context, request))

def view_bookings(request):
	bookings = Booking.objects.all()
	template = loader.get_template('view_bookings.html')
	context = {
	   'bookings': bookings,
	}
	return HttpResponse(template.render(context, request))

def view_booking(request, booking_id):
	#return HttpResponse("You're looking at booking %s." % booking_id)
	bookings = Booking.objects.all()
	booking = Booking.objects.get(id=booking_id)
	template = loader.get_template('view_booking.html')
	context = {
	   'booking': booking,
	}
	return HttpResponse(template.render(context, request))



def view_bands (request):


