from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView

from .models import ClockInOut

import datetime



class HomePageView(TemplateView):

    template_name = 'home.html'

class ClockInOutView(ListView):

    model = ClockInOut

    template_name = 'clock_in_out.html'

    fields = ('author', 'notes',)

def timelog(request):

    if request.method == "POST":

        log = ClockInOut(request.POST)

        if form.is_valid():

            return render(request, 'timeclock/clock_in_out.html', context)
                

        
