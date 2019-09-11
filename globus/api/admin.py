from django.contrib import admin
from .models import Driver, Job, Load, Loadtype, Location, Truck, Trailer, Keypersonnel

# Register your models here.
admin.site.register({Driver, Job, Load, Loadtype, Location, Truck, Trailer, Keypersonnel})
