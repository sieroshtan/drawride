from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Follow


@login_required
def follow(request, username):
    if request.META.get("HTTP_ACCEPT") != "text/html+partial":
        raise Http404

    follower = request.user
    followee = get_user_model().objects.get(username=username)

    Follow.objects.add_follower(follower, followee)

    return render(request, "follow/unfollow.html", {"profile": followee})


@login_required
def unfollow(request, username):
    if request.META.get("HTTP_ACCEPT") != "text/html+partial":
        raise Http404

    follower = request.user
    followee = get_user_model().objects.get(username=username)

    Follow.objects.remove_follower(follower, followee)

    return render(request, "follow/follow.html", {"profile": followee})


class FollowersView(DetailView):
    model = get_user_model()
    slug_field = "username"
    context_object_name = "profile"
    template_name = "follow/followers.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FollowersView, self).get_context_data(**kwargs)
        context["followers"] = Follow.objects.followers(self.get_object())
        context["follows"] = Follow.objects.follows(self.request.user, self.get_object())
        return context


class FollowingView(DetailView):
    model = get_user_model()
    slug_field = "username"
    context_object_name = "profile"
    template_name = "follow/following.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FollowingView, self).get_context_data(**kwargs)
        context["following"] = Follow.objects.following(self.get_object())
        context["follows"] = Follow.objects.follows(self.request.user, self.get_object())
        return context
