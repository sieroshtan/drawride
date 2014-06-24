import json

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from follow.models import Follow
from .models import Ride, RideMembers, UserFavorites
from .forms import RideForm
from views.base import AuthRequiredMixin


class RideDrawView(AuthRequiredMixin, CreateView):
    form_class = RideForm
    template_name = 'rides/draw.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.city is None:
            messages.error(self.request, _("Before adding the ride please select your city."))
            return redirect('change_city')
        return super(RideDrawView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.city = self.request.user.city
        form.instance.save()

        RideMembers(user=self.request.user, ride=form.instance).save()

        messages.success(self.request, _("You ride has been added."))
        return super(RideDrawView, self).form_valid(form)


class RideEditView(AuthRequiredMixin, UpdateView):
    model = Ride
    form_class = RideForm
    template_name = 'rides/edit.html'

    def get(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            raise Http404
        return super(RideEditView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, _("Edit"))
        return super(RideEditView, self).form_valid(form)


class RideView(DetailView):
    model = Ride
    template_name = 'rides/ride.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RideView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context['is_member'] = RideMembers.objects.is_member(user=self.request.user,
                                                                 ride=self.get_object())
            context['is_favorite'] = UserFavorites.objects.is_favorite(user=self.request.user,
                                                                       ride=self.object)
        return context


class RideDeleteView(DeleteView):
    model = Ride
    success_url = reverse_lazy('rides')


class RidesView(ListView):
    model = Ride
    context_object_name = 'rides'
    paginate_by = 8
    template_name = 'rides/rides.html'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            following = Follow.objects.following(self.request.user)
            return Ride.objects.filter(user__in=following)

        return Ride.objects.popular(self.request.user)


class RidesPopularView(ListView):
    model = Ride
    context_object_name = 'rides'
    paginate_by = 8
    template_name = 'rides/popular.html'

    def get_queryset(self):
        return self.model.objects.popular(self.request.user)


class RidesUpcomingView(ListView):
    model = Ride
    context_object_name = 'rides'
    paginate_by = 8
    template_name = 'rides/upcoming.html'

    def get_queryset(self):
        return self.model.objects.upcoming(self.request.user)


@login_required
def join(request, pk):
    if request.is_ajax() is False:
        raise Http404

    ride = get_object_or_404(Ride, pk=pk)

    response = {'status': 'OK'}

    try:
        ride_member = RideMembers.objects.get(user=request.user, ride=ride)
        ride_member.delete()
    except RideMembers.DoesNotExist:
        ride_member = RideMembers(user=request.user, ride=ride)
        ride_member.save()
    else:
        response['status'] = 'NO'

    members = ride.members.all()

    response['members'] = render_to_string('rides/members.html', {'members': members})

    return HttpResponse(json.dumps(response),
                        content_type='application/json')


@login_required
def fave(request, pk):
    if request.is_ajax() is False:
        raise Http404

    ride = get_object_or_404(Ride, pk=pk)

    response = {'status': 'OK'}

    try:
        fave = UserFavorites.objects.get(user=request.user, ride=ride)
        fave.delete()
    except UserFavorites.DoesNotExist:
        fave = UserFavorites(user=request.user, ride=ride)
        fave.save()
    else:
        response['status'] = 'NO'

    return HttpResponse(json.dumps(response),
                        content_type='application/json')


def ride_export(request, pk, ext):
    ride = get_object_or_404(Ride, pk=pk)

    points = ride.points.split(',')
    coords = list(zip(points[::2], points[1::2]))

    xml = render_to_string('rides/exporters/%s.xml' % ext, {'ride': ride,
                                                            'coords': coords})

    response = HttpResponse(xml, content_type='text/%s+xml' % ext)
    response['Content-Disposition'] = 'attachment; filename=route_%s.%s' % (ride.id, ext)

    return response
