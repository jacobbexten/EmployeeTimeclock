from django.urls import path

from .views import HomePageView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),

    path('time', HomePageView.as_view(), name='time'),

    path('calendar', HomePageView.as_view(), name='calendar'),

]
