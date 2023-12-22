from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _


class MessageForm(forms.ModelForm):
    text = forms.CharField(
        label=_("Your message"),
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": _("Enter your message here...")}),
    )

    class Meta:
        model = Message
        exclude = ("from_user", "to_user")
