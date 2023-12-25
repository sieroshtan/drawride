from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from rides.models import Ride


class AboutView(TemplateView):
    template_name = "main/about.html"


def faq(request):
    ride = get_object_or_404(Ride, pk=1)
    return render(request, "main/faq.html", {"ride": ride})
