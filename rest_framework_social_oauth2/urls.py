# -*- coding: utf-8 -*-

try:
    from django.conf.urls import url, include
except ImportError:
    from django.urls import include, re_path as url
from oauth2_provider.views import AuthorizationView

from .views import ConvertTokenView, TokenView, RevokeTokenView, invalidate_sessions

urlpatterns = [
    url(r'^authorize/?$', AuthorizationView.as_view(), name="authorize"),
    url(r'^token/?$', TokenView.as_view(), name="token"),
    url('', include('social_django.urls', namespace="social")),
    url(r'^convert-token/?$', ConvertTokenView.as_view(), name="convert_token"),
    url(r'^revoke-token/?$', RevokeTokenView.as_view(), name="revoke_token"),
    url(r'^invalidate-sessions/?$', invalidate_sessions, name="invalidate_sessions")
]
