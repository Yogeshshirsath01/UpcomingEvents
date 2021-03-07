from django.contrib import admin
from .models import Event
from django.db import models


# class AdminEvent(admin.ModelAdmin):
#    list_display = ['event_name', 'description',
#                    'date', 'location', 'time', 'is_liked']


admin.site.register(Event)
