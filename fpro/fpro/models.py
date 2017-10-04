from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Scene(models.Model):
        sceneName = models.CharField(max_length=100)

        def __str__(self):
                return self.sceneName


class Genre(models.Model):
		genreName = models.CharField(max_length = 100, blank=True, default="")
		def __str__(self):
			return self.genreName


class Band(models.Model):
        bandName = models.CharField(max_length=100)
        StreamCount = models.IntegerField(default = 0)
        Visits = models.IntegerField(default = 0)
        genre = models.ForeignKey(Genre, null=True, blank=True)

        def __str__(self):
                return self.bandName

class Booking(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	date = models.DateField('date playing')
	approvedBookingBoss = models.BooleanField(default=False)
	approvedManager = models.BooleanField(default=False)
	technicalRequirements = models.CharField(max_length=100, blank=True, default="")
	scene = models.ForeignKey(Scene, on_delete=models.CASCADE, blank=True)
	ticketPrice = models.DecimalField(max_digits=30, decimal_places=2, default=0)
	technicians = models.ManyToManyField(User, blank=True)
	managerEmail = models.CharField(max_length=100, blank=True)
	# ticketPrice = models.DecimalField(max_digits=30, decimal_places=2, default = 0)
	bandPrice = models.DecimalField(max_digits=30, decimal_places=2, default = 0)
	otherCosts = models.DecimalField(max_digits=30, decimal_places=2, default = 0)
	ticketsSold = models.IntegerField(default = 0)


	def totalCostResult(self):
		return self.ticketPrice * self.ticketsSold - self.bandPrice - self.otherCosts

	def totalCost(self):
		return self.bandPrice + self.otherCosts

	def __str__(self):
                return self.band.bandName + " playing at " + str(self.date) + " at scene " + self.scene.sceneName
