from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from django.contrib.auth.models import User
from .models import Booking, Scene, Band


# Create your views here.
#def addBookingInDb(request):


def send_email(request):
	manager = request.POST.get('name')
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
	bookings = Booking.objects.all()
	user = request.user
	user_bookings = []

	for booking in bookings:
		if user in booking.technicians.all():
			user_bookings += [booking]

	print(user_bookings)

	template = loader.get_template('shifts.html')
	context = {
	 	'bookings': bookings,
		'user_bookings' : user_bookings,
	}
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

def concert_overview(request):
	bookings = Booking.objects.all()
	scenes = Scene.objects.all()
	bookings_array = {}
	for scene in scenes:
		for booking in bookings:
			if booking.scene == scene:
				bookings_array[scene] = []
				bookings_array[scene] += [booking]

	template = loader.get_template("concert_overview.html")
	context = {
		'scenes' : scenes,
	  	'bookings': bookings,
		'bookings_array': bookings_array,
	}

	return HttpResponse(template.render(context, request))
