from django import forms
from .models import *
from django.contrib.auth.models import User
import datetime

class CreateBookingForm(forms.Form):
	band = forms.ModelChoiceField(queryset=Band.objects, label="Choose band", required=False)
	bandName = forms.CharField(label="or specify new band name", max_length=100, required=False)
	managerEmail = forms.EmailField()
	date = forms.DateField(label="Date", initial=datetime.date.today, widget=forms.SelectDateWidget)
	price = forms.DecimalField(label="Price")
	scene = forms.ModelChoiceField(queryset=Scene.objects)


class AddShiftForm(forms.Form):
	technician = forms.ModelChoiceField(queryset=User.objects, label="Choose technician", required=True)
	booking = forms.ModelChoiceField(queryset=Booking.objects, label="Choose booking", required=True)
    

class SendTechneedsForm(forms.Form):
    booking = forms.ModelChoiceField(queryset=Booking.objects, label="Choose booking", required=True)
    techneeds = forms.CharField(label="Specify your techical needs", max_length=100, required=True)
