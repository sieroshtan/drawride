from django.urls import path, re_path
from .views import SignUpView, ActivationView
from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from registration.views import PasswordResetViewCustom, PasswordResetConfirmViewCustom

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    re_path(
        r"^activate/(?P<activation_key>\w+)$",
        ActivationView.as_view(),
        name="registration_activate",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("recover/", PasswordResetViewCustom.as_view(), name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmViewCustom.as_view(),
        name="password_reset_confirm",
    ),
]
