from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import Context, Template
from rides.models import Ride
from .forms import CommentForm


@login_required()
def post_comment(request, ride_id):
    if request.is_ajax() is False:
        raise Http404

    ride = get_object_or_404(Ride, pk=ride_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_object = ride
        comment.user = request.user
        comment.save()

    t = Template('{% load comments %}{% comments ride %}')

    return HttpResponse(t.render(Context({'ride': ride})))
