from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SettingsForm, PhotoForm
from rides.models import Ride
from views.base import AuthRequiredMixin

User = get_user_model()


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users.html'


class ProfileView(DetailView):
    model = User
    slug_field = 'username'
    context_object_name = 'profile'
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['rides'] = Ride.objects.rides().filter(user=self.get_object())
        return context


class ProfileDraftsView(DetailView):
    model = User
    slug_field = 'username'
    context_object_name = 'profile'
    template_name = 'users/drafts.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDraftsView, self).get_context_data(**kwargs)
        context['rides'] = Ride.objects.rides(is_hide=True).filter(user=self.get_object())
        return context


class ProfileInvolvedView(DetailView):
    model = User
    slug_field = 'username'
    context_object_name = 'profile'
    template_name = 'users/involved.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileInvolvedView, self).get_context_data(**kwargs)
        context['rides'] = Ride.objects.rides().filter(members__id=self.get_object().id)
        return context


class ProfileFavoritesView(DetailView):
    model = User
    slug_field = 'username'
    context_object_name = 'profile'
    template_name = 'users/favorites.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileFavoritesView, self).get_context_data(**kwargs)

        rides = self.get_object().favorites.all()

        context['rides'] = rides
        return context


class SettingsView(AuthRequiredMixin, UpdateView):
    form_class = SettingsForm
    success_url = reverse_lazy('settings')
    template_name = 'users/settings.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, _("Profile information has been changed."))
        return super(SettingsView, self).form_valid(form)


class SettingsPasswordView(AuthRequiredMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('settings_password')
    template_name = 'users/password.html'

    def get_form_kwargs(self):
        kwargs = super(SettingsPasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, _('Your settings have been saved!'))
        return super(SettingsPasswordView, self).form_valid(form)


class SettingsPhotoView(AuthRequiredMixin, UpdateView):
    form_class = PhotoForm
    success_url = reverse_lazy('settings_photo')
    template_name = 'users/photo.html'

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            user = self.get_object()
            user.photo = ''
            user.save()
            messages.success(self.request, _("Your photo have been removed!"))
            return redirect('settings_photo')
        return super(SettingsPhotoView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, _("Your settings have been saved!"))
        return super(SettingsPhotoView, self).form_valid(form)
