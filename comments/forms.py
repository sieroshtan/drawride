from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": "3", "placeholder": _("Enter your comment here...")})
    )

    class Meta:
        model = Comment
        fields = ("text",)
