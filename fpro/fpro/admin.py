from django.contrib import admin

# Register your models here.

from .models import Booking
from .models import Scene
from .models import Band
from .models import Genre
from .models import Festival

admin.site.register(Booking)
admin.site.register(Scene)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Festival)
