from django.contrib import admin

from app.models import Appointment, Doctor


# Register your models here.

admin.site.register(Doctor)

admin.site.register(Appointment)
