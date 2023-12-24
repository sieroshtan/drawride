from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from rides.models import Ride
from .forms import CommentForm
from comments.models import Comment


@login_required()
def post_comment(request, ride_id):
    if request.META.get("HTTP_X_REQUESTED_WITH") != "XMLHttpRequest":
        raise Http404

    ride = get_object_or_404(Ride, pk=ride_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_object = ride
        comment.user = request.user
        comment.save()

    comment_type = ContentType.objects.get_for_model(ride)
    comments = Comment.objects.filter(content_type__pk=comment_type.id, object_id=ride.id)

    return render(request, "comments/comments.html", {"comments": comments})
