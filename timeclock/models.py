from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse


class Clockin(models.Model):

    author = models.ForeignKey(

        get_user_model(),

        on_delete=models.CASCADE,

    )

    date = models.DateTimeField(auto_now_add=True)

    notes = models.CharField(max_length=100, default='', blank=True)


