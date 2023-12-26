from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Ride


class RideForm(forms.ModelForm):
    title = forms.CharField(label=_("Title"))

    points = forms.CharField(
        widget=forms.HiddenInput(),
        error_messages={"required": "Please draw you route."},
    )

    distance = forms.CharField(
        label=_("Distance"),
        initial="0.00",
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )

    description = forms.CharField(
        label=_("Description"),
        required=False,
        max_length=1000,
        widget=forms.Textarea(attrs={"rows": "7"}),
    )

    start_date = forms.DateField(
        label=_("Start Date"),
        required=False,
        help_text=_("Optional"),
    )

    end_date = forms.DateField(
        label=_("End Date"),
        required=False,
        help_text=_("Optional"),
    )

    class Meta:
        model = Ride
        exclude = ("user", "city", "members", "favorites")
