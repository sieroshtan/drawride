from django.views.generic import CreateView
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.template.response import TemplateResponse
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from .forms import RegistrationForm, SetNewPasswordForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, _("Registration success"))
        return super(RegisterView, self).form_valid(*args, **kwargs)


def custom_password_reset(request):
    response = password_reset(request,
                              template_name='registration/recover.html',
                              email_template_name='registration/reset_email.html',
                              post_reset_redirect='home')

    if not isinstance(response, TemplateResponse):
        messages.success(request, _("We have sent you the email with reset password instructions"))

    return response


def custom_password_reset_confirm(request, uidb64, token):
    response = password_reset_confirm(request,
                                      uidb64,
                                      token,
                                      'registration/reset_confirm.html',
                                      set_password_form=SetNewPasswordForm,
                                      post_reset_redirect='login')

    if not isinstance(response, TemplateResponse):
        messages.success(request, _("Your password has been changed. Please use your new password to login"))

    return response
