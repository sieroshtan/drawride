from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Ride


class RideForm(forms.ModelForm):
    title = forms.CharField(label=_("Title"))

    points = forms.CharField(widget=forms.HiddenInput(),
                             error_messages={'required': "Please draw you route."})

    distance = forms.CharField(label=_("Distance"),
                               initial='0.00',
                               widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    description = forms.CharField(label=_("Description"),
                                  required=False,
                                  max_length=1000,
                                  widget=forms.Textarea(attrs={'rows': '7'}))

    start_time = forms.DateTimeField(label=_("Start Time"),
                                     widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class': 'datetime'}))

    end_time = forms.DateTimeField(label=_("End Time"),
                                   required=False,
                                   widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class': 'datetime'}),
                                   help_text=_("Optional field"))

    class Meta:
        model = Ride
        exclude = ('user', 'city', 'members', 'favorites')
