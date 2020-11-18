from django.contrib import admin

from django.urls import path

from .views import HomePageView, ClockInOutView, EventView, AddClockInOutView, AllEntriesView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),

    path('clock_in_out/', AddClockInOutView.as_view(), name = 'clock_in_out'),

    path('clock_in_out/entries/', ClockInOutView.as_view(), name='entries'),

    path('calendar/', EventView.as_view(), name='calendar'),

    path('clock_in_out/entries/all_entries/', AllEntriesView.as_view(), name = 'all_entries'),

]
