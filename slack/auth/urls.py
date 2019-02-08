from django.conf.urls import url

from slack.auth import views

urlpatterns = [
    url(r"^u/([^/]+)/$", views.slack_redirect),
    url(r"^slack-domain-not-allowed/$", views.not_allowed),
    url(r"get_additional_permissions/$", views.get_additional_permissions),
]
