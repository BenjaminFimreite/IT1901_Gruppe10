from django.contrib import admin

# Register your models here.

from .models import Booking
from .models import Scene
from .models import Band

admin.site.register(Booking)
admin.site.register(Scene)
admin.site.register(Band)
