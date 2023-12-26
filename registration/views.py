from django.views.generic import CreateView, RedirectView, DetailView
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.conf import settings
from .forms import RegistrationForm, SetNewPasswordForm


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, *args, **kwargs):
        messages.success(
            self.request,
            _(
                "You should receive a welcome email from us. Please click the link within to confirm your account."
            ),
        )
        return super(SignUpView, self).form_valid(*args, **kwargs)


class ActivationView(RedirectView):
    permanent = False

    def get_redirect_url(self, activation_key, *args, **kwargs):
        user = get_object_or_404(get_user_model(), activation_key=self.kwargs["activation_key"])
        user.activate()

        messages.success(self.request, _("Your email address has been confirmed. Thanks!"))
        login(self.request, user)

        return reverse_lazy("home")


class PasswordResetViewCustom(PasswordResetView):
    email_template_name = "registration/reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"
    template_name = "registration/recover.html"
    success_url = "/"

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(
            self.request,
            _("We have sent you the email with reset password instructions"),
        )
        return res


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    form_class = SetNewPasswordForm
    template_name = "registration/reset_confirm.html"
    success_url = settings.LOGIN_URL

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(
            self.request,
            _("Your password has been changed. Please use your new password to login"),
        )
        return res
