from django.views.generic import ListView, DetailView, RedirectView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Country, City

User = get_user_model()


class CitiesView(ListView):
    model = Country
    context_object_name = 'countries'
    template_name = 'geo/cities.html'

    def get_queryset(self):
        return self.model.objects.prefetch_related('cities')


class CityView(DetailView):
    model = City
    template_name = 'geo/city.html'


class CityPeopleView(DetailView):
    model = City
    template_name = 'geo/people.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CityPeopleView, self).get_context_data(**kwargs)
        context['users'] = User.objects.filter(city=self.object)
        return context


class ChangeCityView(ListView):
    model = Country
    context_object_name = 'countries'
    template_name = 'geo/change_city.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChangeCityView, self).dispatch(*args, **kwargs)


class SetCityView(RedirectView):
    permanent = False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SetCityView, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, pk):
        city = get_object_or_404(City, pk=pk)
        self.request.user.city = city
        self.request.user.save()
        return reverse('home')
