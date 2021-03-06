from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import json

# Create your models here.

class Scene(models.Model):
    sceneName = models.CharField(max_length=100)

    def __str__(self):
        return self.sceneName


class Genre(models.Model):
    genreName = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.genreName


class Band(models.Model):
    bandName = models.CharField(max_length=100, default="")
    streamCount = models.IntegerField(default=0)
    visits = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, null=True, blank=True)
    albumSales = models.IntegerField(default=0)

    def __str__(self):
        return self.bandName


class Booking(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    date = models.DateField('date playing')
    approvedBookingBoss = models.BooleanField(default=False)
    approvedManager = models.BooleanField(default=False)
    technicalRequirements = models.CharField(max_length=100, blank=True, default="")
    completedTechnicalRequirements = models.CharField(max_length=100, blank=True, default="")
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, blank=True)
    ticketPrice = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    technicians = models.ManyToManyField(User, blank=True)
    managerEmail = models.CharField(max_length=100, blank=True)
    bandPrice = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    otherCosts = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    ticketsSold = models.IntegerField(default=0)
    review = models.CharField(max_length=500, blank=True, default="")
    Songs = models.CharField(max_length=1000, blank=True, default="")
    pressLink = models.CharField(max_length=1000, blank=True, default="")

    techAtt = models.CharField(max_length=1000, blank=True, default="[]")
    techUnatt= models.CharField(max_length=1000, blank=True, default="[]")

    def getTechAtt(self):
        ta = json.loads(self.techAtt)
        return ta

    def getTechUnatt(self):
        tua = json.loads(self.techUnatt)
        return tua

    def addTechAtt(self, user_id):
        ta = json.loads(self.techAtt)
        if user_id not in ta:
            ta.append(user_id)
        self.techAtt = json.dumps(ta)

    def addTechUnatt(self, user_id):
        tua = json.loads(self.techUnatt)
        if user_id not in tua:
            tua.append(user_id)
        self.techUnatt = json.dumps(tua)

    def totalCostResult(self):
        return self.ticketPrice * self.ticketsSold - self.bandPrice - self.otherCosts

    def totalCost(self):
        return self.bandPrice + self.otherCosts

    def inFuture(self):
        return self.date >= datetime.now().date()

    def __str__(self):
        if len(self.technicians.all()) > 0:
            return self.band.bandName + " playing at " + str(self.date) + " at scene " + self.scene.sceneName + " (Tech Contact: " + str(self.technicians.all()[0]) +  ")"
        else:
            return self.band.bandName + " playing at " + str(self.date) + " at scene " + self.scene.sceneName + " (No tech contact)"

class Festival(models.Model):
	startDate = models.DateField("startDate")
	endDate = models.DateField("endDate")
