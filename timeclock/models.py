from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse

from datetime import date

from django.utils import timezone

from django import forms

import calendar

from calendar import HTMLCalendar

from django.utils.safestring import mark_safe


class ClockInOut(models.Model):

    author = models.ForeignKey(

        get_user_model(),

        on_delete=models.CASCADE,

    )

    time = models.TimeField(default=timezone.localtime)

    date = models.DateField(default=date.today)

    notes = models.CharField(max_length=100, default='', blank=True)

    option=(

        ('CLOCKED IN AT ',"Clock In"),

        ('CLOCKED OUT AT',"Clock Out")

    )


    options = models.CharField(max_length=14, choices=option,default="Clocked in at")



    def get_absolute_url(self):

        return 'entries'

 
 
class Event(models.Model):
    day = models.DateField(u'Time Off Request', help_text=u'Time Off Request')
    notes = models.TextField(u'Notes', help_text=u'Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def get_absolute_url(self):
        return 'calendar'

    list_display = ['day', 'notes']
    change_list_template = 'calendar.html'

    def changelist_view(self, request, extra_context=None):
        after_day = request.GET.get('day__gte', None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1)  # find first day of previous month

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + datetime.timedelta(days=1)  # forward a single day
        next_month = datetime.date(year=next_month.year, month=next_month.month,
		           day=1)  # find first day of next month

        extra_context['previous_month'] = reverse('timeclock_event_changelist') + '?day__gte=' + str(previous_month)
        extra_context['next_month'] = reverse('timeclock_event_changelist') + '?day__gte=' + str(next_month)

        cal = HTMLCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
        extra_context['calendar'] = mark_safe(html_calendar)
        return super(Event, self).changelist_view(request, extra_context)


