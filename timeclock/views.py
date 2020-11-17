from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView

from .models import ClockInOut, Event

import datetime



class HomePageView(TemplateView):

    template_name = 'home.html'


class ClockInOutView(ListView):

    model = ClockInOut

    template_name = 'entries.html'

class AllEntriesView(ListView):

    model = ClockInOut

    template_name = 'all_entries.html'

class AddClockInOutView(CreateView):

    model = ClockInOut

    template_name = 'clock_in_out.html'

    fields = ('options','notes',)

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

class EventView(ListView):

    model = Event

    template_name = 'calendar.html'

    fields = '__all__'


               

        
