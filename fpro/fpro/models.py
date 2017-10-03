from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Scene(models.Model):
        sceneName = models.CharField(max_length=100)

        def __str__(self):
                return self.sceneName

class Band(models.Model):
        bandName = models.CharField(max_length=100)
        StreamCount = models.CharField(default = '', max_length = 250)
        Visits = models.CharField(default = '', max_length = 500)
        Genre = models.CharField(max_length = 500)

        def __str__(self):
                return self.bandName + self.StreamCount + self.Visits

class Booking(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	date = models.DateField('date playing')
	approvedBookingBoss = models.BooleanField(default=False)
	approvedManager = models.BooleanField(default=False)
	technicalRequirements = models.CharField(max_length=100, blank=True, default="")
	scene = models.ForeignKey(Scene, on_delete=models.CASCADE, blank=True)
	pris = models.DecimalField(max_digits=30, decimal_places=2)
	technicians = models.ManyToManyField(User, blank=True)
	managerEmail = models.CharField(max_length=100, blank=True)

	def __str__(self):
                return self.band.bandName + " playing at " + str(self.date) + " at scene " + self.scene.sceneName


