from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView

from .models import Clockin



class HomePageView(TemplateView):

    template_name = 'home.html'

class ClockInOutView(ListView):

    model = Clockin

    template_name = 'clock_in_out.html'

    fields = ('author', 'notes',)
