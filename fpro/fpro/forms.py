from django import forms
from .models import *
from django.contrib.auth.models import User
import datetime
from .roles import *
from rolepermissions.checkers import has_permission


class CreateBookingForm(forms.Form):
    band = forms.ModelChoiceField(queryset=Band.objects.values_list('bandName', flat=True), label="Choose band",
                                  required=False)
    bandName = forms.CharField(label="or specify new band name", max_length=100, required=False)
    managerEmail = forms.EmailField()
    date = forms.DateField(label="Date", initial=datetime.date.today, widget=forms.SelectDateWidget)
    price = forms.DecimalField(label="Price")  # bandPrice
    ticketPrice = forms.DecimalField(label="Ticket Price")
    scene = forms.ModelChoiceField(queryset=Scene.objects)


class AddShiftForm(forms.Form):
    users = User.objects.all()
    techs = []
    for user in users:
        if has_permission(user, 'view_my_shifts'):
            techs.append(user.id)
    del techs[techs.index(1)]
    technician = forms.ModelChoiceField(queryset=User.objects.filter(id__in=techs), label="Choose technician",
                                        required=True)
    booking = forms.ModelChoiceField(queryset=Booking.objects.filter(date__gte=datetime.datetime.now().date()).filter(approvedBookingBoss=True).filter(approvedManager=True),
                                     label="Choose booking", required=True)


class SendTechneedsForm(forms.Form):
    booking = forms.ModelChoiceField(queryset=Booking.objects.filter(date__gte=datetime.datetime.now().date()),
                                     label="Choose booking:", required=True)
    techneeds = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}), label="Specify your technical needs:",
                                max_length=100, required=True)
    
    
class SendReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}), label="Specify your technical needs:",
                                max_length=100, required=True)
    
    
class SendSongsForm(forms.Form):
    booking = forms.ModelChoiceField(queryset=Booking.objects.filter(date__gte=datetime.datetime.now().date()),
                                     label="Choose booking:", required=True)
    songs = forms.CharField(widget=forms.Textarea(attrs={'rows': '10'}), label="Specify your song:",
                                max_length=100, required=True)
