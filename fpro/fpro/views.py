from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.models import User
from .models import Booking, Scene, Band
from .forms import *

from datetime import datetime


# Create your views here.
# def pending_bookings():
#	bookings =  Booking.objects.get(approvedBookingBoss=false)
#	template = loader.get_template('pending_bookings.html')
#	context = {
#	   'bookings': bookings
#	}
#	return HttpResponse(template.render(context, request))

def send_email(booking):
    print("hei")
    manager = booking.managerEmail  # request.POST.get('name')
    price = booking.bandPrice  # request.POST.get('price')
    date = booking.date
    band = booking.band
    scene = booking.scene
    msg = "Prisforslag: " + str(price) + "\n" + "Dato:" + str(date) + "\n" + str(band) + "\n" + str(scene)
    sender = 'fpro.no'
    subject = 'Bookingtilbud'
    if price and manager:
        try:
            send_mail(subject, msg, sender, [manager])
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponseRedirect('/pending_bookings')
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

    bookings = Booking.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateBookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)  # a dictionary
            b_form = Booking()  # lager ny booking
            if form.cleaned_data["bandName"] != "":
                band_temp = Band()
                band_temp.bandName = form.cleaned_data["bandName"]
                band_temp.save()
                b_form.band = band_temp
            else:
                b_form.band = form.cleaned_data["band"]
            b_form.date = form.cleaned_data["date"]
            b_form.bandPrice = form.cleaned_data["price"]
            b_form.scene = form.cleaned_data["scene"]
            b_form.managerEmail = form.cleaned_data["managerEmail"]
            b_form.ticketPrice = form.cleaned_data["ticketPrice"]

            if b_form not in bookings:
                b_form.save()
                # redirect to a new URL:
                return HttpResponse("Booking successfully created")
            else:
                b_form.delete()
                return HttpResponse("Booking already exists")
                # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateBookingForm()

    context = {
        'form': form

    }
    return HttpResponse(template.render(context, request))


def shifts(request):
    bookings = Booking.objects.all()
    user = request.user
    user_bookings = []
    template = loader.get_template('shifts.html')

    if request.method == 'POST':
        form = AddShiftForm(request.POST)
    # if form.is_valid():
    # break
    else:
        form = AddShiftForm()

    for booking in bookings:
        if user in booking.technicians.all():
            user_bookings += [booking]

    print(user_bookings)

    context = {
        'form': form,
        'bookings': bookings,
        'user_bookings': user_bookings,
    }
    return HttpResponse(template.render(context, request))


def bookings(request):
    bookings = Booking.objects.all()
    template = loader.get_template('bookings.html')
    context = {
        'bookings': bookings,
    }
    return HttpResponse(template.render(context, request))


def booking(request, booking_id):
    # return HttpResponse("You're looking at booking %s." % booking_id)
    bookings = Booking.objects.all()
    booking = Booking.objects.get(id=booking_id)
    template = loader.get_template('booking.html')
    context = {
        'booking': booking,
    }
    return HttpResponse(template.render(context, request))


def pending_bookings(request):
    bookings = Booking.objects.all()

    # Lag array med alle pending bookings (ikke godkjent av bookingsjef)
    print(request.GET.get("value", ""))
    print(request.GET.get("booking", ""))
    # Booking accepted
    if request.GET.get("value", "") == "accepted" and Booking.objects.filter(
            id=request.GET.get("booking", "")).count() > 0:
        booking = Booking.objects.get(id=request.GET.get("booking", ""))
        booking.approvedBookingBoss = True
        send_email(booking)
        booking.save()
        return HttpResponseRedirect("/bookings/pending_bookings")
    # Booking declined
    elif request.GET.get("value", "") == "declined" and Booking.objects.filter(
            id=request.GET.get("booking", "")).count() > 0:
        booking = Booking.objects.get(id=request.GET.get("booking", ""))
        booking.delete()
        return HttpResponseRedirect("/bookings/pending_bookings")
    elif request.GET.get("value", "") == "declined" or request.GET.get("value", "") == "accepted":
        return HttpResponseRedirect("/bookings/pending_bookings")

    pending_bookings_array = []
    for booking in bookings:
        if not booking.approvedBookingBoss:
            pending_bookings_array += [booking]

    approved_by_bookingboss = []
    for booking in bookings:
        if booking.approvedBookingBoss and not booking.approvedManager:
            approved_by_bookingboss += [booking]

    template = loader.get_template('pending_bookings.html')
    context = {
        'bookings': bookings,
        'pending_bookings_array': pending_bookings_array,
        'approved_by_bookingboss': approved_by_bookingboss,
    }

    return HttpResponse(template.render(context, request))


def bands(request):
    bands = Band.objects.all()
    template = loader.get_template('bands.html')
    context = {
        'bands': bands,
    }
    return HttpResponse(template.render(context, request))


def band(request, band_id):
    bands = Band.objects.all()
    band = Band.objects.get(id=band_id)
    template = loader.get_template('band.html')
    context = {
        'band': band,
    }
    return HttpResponse(template.render(context, request))


def overview(request):
    bookings = Booking.objects.all()
    scenes = Scene.objects.all()
    genres = Genre.objects.all()
    coming_bookings = {}
    past_bookings = []
    festival = None
    if festival:
        festival = Festival.objects.all()[0]

    for scene in scenes:
        coming_bookings[scene] = []
        for booking in bookings:
            if (booking.scene == scene) and booking.approvedManager and booking.approvedBookingBoss and booking.date >= datetime.now().date():
                # coming_bookings[scene] = []
                coming_bookings[scene] += [booking]
    for booking in bookings:
        if booking.approvedBookingBoss and booking.date < datetime.now().date():
            past_bookings += [booking]

    #totalConsertDates = (festival.endDate - festival.startDate).days
    dates = set()
    for b in bookings:
        dates.add(b.date)
    #freeConsertDates = totalConsertDates - len(dates)


    template = loader.get_template("overview.html")
    context = {
        'past_bookings': past_bookings,
        'scenes': scenes,
        'bookings': bookings,
        'bookings_array': coming_bookings,
        'genres': genres,
		'futureBookingsCount' : len(coming_bookings),
		'festival' : festival,
		#'totalConsertDates' : totalConsertDates,
		#'freeConsertDates' : freeConsertDates,
    }

    return HttpResponse(template.render(context, request))


def genre(request):
    genres = Genre.objects.all()
    template = loader.get_template('Genres.html')
    context = {
        'genres': genres,
    }
    return HttpResponse(template.render(context, request))


def send_techneeds(request):
    bookings = Booking.objects.all()
    template = loader.get_template("send_techneeds.html")

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SendTechneedsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)  # a dictionary
            booking = form.cleaned_data["booking"]  # henter valgt booking
            if booking.technicalRequirements is not None:
                booking.technicalRequirements += '\n'
            booking.technicalRequirements += form.cleaned_data["techneeds"]
            booking.save()
            # redirect to a new URL:
            return HttpResponse("Techneeds successfully sent")
            # if a GET (or any other method) we'll create a blank form
    else:
        form = SendTechneedsForm()
    context = {
        'bookings': bookings,
        'form': form,
    }
    return HttpResponse(template.render(context, request))
