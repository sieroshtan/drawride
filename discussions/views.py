from django.views.generic import CreateView, ListView
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import MessageContact, Message
from views.base import AuthRequiredMixin


@require_http_methods(["POST"])
@login_required
def compose(request, username):
    if request.META.get("HTTP_ACCEPT") != "text/html+partial":
        raise Http404

    to_user = get_object_or_404(get_user_model(), username=username)
    form = MessageForm(request.POST)

    if form.is_valid():
        message = form.save(commit=False)
        message.from_user = request.user
        message.to_user = to_user
        message.save()

    return render(request, "discussions/ts/compose.html")


class DiscussionsView(AuthRequiredMixin, ListView):
    model = MessageContact
    context_object_name = "discussions"
    template_name = "discussions/discussions.html"

    def get_queryset(self):
        return self.model.objects.get_contacts_for(self.request.user)


class DiscussionView(AuthRequiredMixin, CreateView):
    form_class = MessageForm
    slug_field = "username"
    template_name = "discussions/discussion.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DiscussionView, self).get_context_data(**kwargs)
        contact = get_object_or_404(get_user_model(), username=self.kwargs["username"])

        context["contact"] = contact
        context["messages_list"] = Message.objects.get_conversation_between(
            self.request.user, contact
        )

        return context

    def form_valid(self, form):
        to_user = get_object_or_404(get_user_model(), username=self.kwargs["username"])
        form.instance.from_user = self.request.user
        form.instance.to_user = to_user
        return super(DiscussionView, self).form_valid(form)

    def get_success_url(self):
        return reverse("discussion", args=(self.kwargs["username"],))
