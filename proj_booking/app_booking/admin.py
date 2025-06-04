from django.contrib import admin
from .models import SportsClub, Sport, Slot

# Register your models here.

admin.site.register([
   
    SportsClub,
    Sport,
    Slot
    # Add your models here
])