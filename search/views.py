from django.views.generic import ListView
from django.http import Http404
from rides.models import Ride


class SearchView(ListView):
    model = Ride
    context_object_name = 'rides'
    paginate_by = 8
    template_name = 'search/search.html'

    def get_queryset(self):
        if 'q' in self.request.GET and self.request.GET['q']:
            q = self.request.GET['q'].strip()
            return Ride.objects.filter(title__icontains=q)
        raise Http404

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['search_q'] = self.request.GET.get('q')
        return context
