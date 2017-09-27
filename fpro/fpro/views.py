from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import BandInfo
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from .models import Booking, Scene, Band
from .forms import *


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

def create_booking2(request):
	template = loader.get_template('create_booking2.html')

		# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CreateBookingForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			print(form.cleaned_data)	# a dictionary
			b_form = Booking()
			if form.cleaned_data["bandName"] != "":
				band_temp = Band()
				band_temp.bandName = form.cleaned_data["bandName"]
				band_temp.save()
				b_form.band = band_temp
			else:
				b_form.band = form.cleaned_data["band"]
			b_form.date = form.cleaned_data["date"]
			b_form.pris = form.cleaned_data["price"]
			b_form.scene = form.cleaned_data["scene"]

			b_form.save()
			# redirect to a new URL:
			return HttpResponse("Booking successfully created")
	# if a GET (or any other method) we'll create a blank form
	else:
		form = CreateBookingForm()

	context = {
		'form' : form
    }
	return HttpResponse(template.render(context, request))


def shifts(request):
	bookings = Booking.objects.all()
	user = request.user
	user_bookings = []
	template = loader.get_template('shifts.html')

	if request.method == 'POST':
		form = AddShiftForm(request.POST)
#		if form.is_valid():
	#		break
	else:
		form = AddShiftForm()

	for booking in bookings:
		if user in booking.technicians.all():
			user_bookings += [booking]

	print(user_bookings)

	context = {
		'form' : form,
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

def view_bands (request):
    context = {}
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
