from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView

from .models import Clockin



class HomePageView(TemplateView):

    template_name = 'home.html'

class ClockInOutView(CreateView):

    model = Clockin

    template_name = 'clock_in_out.html'

    fields = ('author', 'notes',)
