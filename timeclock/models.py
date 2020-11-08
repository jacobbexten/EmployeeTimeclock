from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse

from datetime import date

from django.utils import timezone


class ClockInOut(models.Model):

    author = models.ForeignKey(

        get_user_model(),

        on_delete=models.CASCADE,

    )

    time = models.TimeField(default=timezone.localtime)

    date = models.DateField(default=date.today)

    notes = models.CharField(max_length=100, default='', blank=True)


    def ge_absolute_url(self):

        return reverse('clock_in_out', args=[str(self.id)])

