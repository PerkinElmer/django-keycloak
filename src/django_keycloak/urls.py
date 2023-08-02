"""resource_provider URL Configuration """

from django.urls import re_path

from django_keycloak import views

urlpatterns = [
    re_path(r'^login$', views.Login.as_view(), name='keycloak_login'),
    re_path(r'^login-complete$', views.LoginComplete.as_view(),
        name='keycloak_login_complete'),
    re_path(r'^logout$', views.Logout.as_view(), name='keycloak_logout'),
    re_path(r'^session-iframe', views.SessionIframe.as_view(),
        name='keycloak_session_iframe')
]
