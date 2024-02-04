from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
from .views import MicrosoftLogin
from rest_auth.registration.views import (
    SocialAccountListView,
    SocialAccountDisconnectView,
)
from rest_auth.registration.views import VerifyEmailView


router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", MicrosoftLogin.as_view(), name="socialaccount_signup"),
    path("refresh-token/", refresh_jwt_token),
    path("me/", SocialAccountListView.as_view()),
    path("socialaccounts/disconnect/", SocialAccountDisconnectView.as_view()),
    re_path(
        r"^account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
]
