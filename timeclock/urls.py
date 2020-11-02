from django.urls import path

from .views import HomePageView, ClockInOutView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),

    path('clock_in_out/', ClockInOutView.as_view(), name='clock_in_out'),

    path('calendar/', HomePageView.as_view(), name='calendar'),

]
