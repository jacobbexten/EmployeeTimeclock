from django import forms

from .models import ClockInOut

class ClockInOutForm(forms.Form):

    option = models.ChoiceField(required=True, widget=forms.RadioSelect())
