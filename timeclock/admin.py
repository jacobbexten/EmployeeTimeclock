from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import ClockInOut, Event

import  datetime

import calendar

from django.urls import reverse

from calendar import HTMLCalendar

from django.utils.safestring import mark_safe



admin.site.register(Event)
admin.site.register(ClockInOut)



