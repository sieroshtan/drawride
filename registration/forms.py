from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import get_user_model


User = get_user_model()

help_text = {'username': _("Username must contain only letters, numbers and underscores"),
             'password': _("Minimum 6 characters"),
             'password2': _("Enter the same password as above, for verification")}

error_mes = {'invalid_username': _("Enter a valid username"),
             'duplicate_username': _("A user with that username already exists"),
             'duplicate_email': _("A user with that email already exists"),
             'password_mismatch': _("The two password fields didn't match"),
             'math_answer': _("Your math is incorrect")}


class RegistrationForm(forms.ModelForm):
    username = forms.RegexField(label=_("Username"),
                                min_length=3,
                                max_length=25,
                                regex=r'^[a-zA-Z0-9_]+$',
                                help_text=help_text['username'],
                                error_messages={'invalid': error_mes['invalid_username']})

    email = forms.EmailField(label=_("Email address"))

    password = forms.CharField(label=_("Password"),
                               min_length=6,
                               widget=forms.PasswordInput,
                               help_text=help_text['password'])

    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=help_text['password2'])

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(error_mes['duplicate_username'])

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(error_mes['duplicate_email'])

    def clean_password2(self):
        password = self.cleaned_data.get('password', None)
        password2 = self.cleaned_data.get('password2', None)
        if password and password2 and (password == password2):
            return password2
        else:
            raise forms.ValidationError(error_mes['password_mismatch'])

    def save(self, *args, **kwargs):
        new_user = User.activation.create_inactive_user(self.cleaned_data['username'],
                                                        self.cleaned_data['email'],
                                                        self.cleaned_data['password'])
        return new_user

    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(MaxLengthValidator(25))


class SetNewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetNewPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].validators.append(MinLengthValidator(6))
        self.fields['new_password1'].help_text = _("Minimum 6 characters")
