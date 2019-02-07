from functools import partial
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from slackclient import SlackClient


def associate_by_slack_name(backend, details, user=None, *args, **kwargs):
    """
    Associate pre-existing users by slack name.
    Useful for prepopulating data from slack api.
    Not recommended if multiple slack domains are used.
    """
    if user:
        return
    username = details["username"]
    if backend.strategy.storage.user.user_exists(username=username):
        return {
            "user": backend.strategy.storage.user.get_user(username=username),
            "is_new": False,
        }


@partial
def validate_team(backend, details, response, is_new=False, *args, **kwargs):
    if backend.name == "slack" and is_new:
        team_id = response["team"]["id"]
        if team_id not in settings.ALLOWED_SLACK_TEAMS:
            url = "/slack-domain-not-allowed/?domain=%s" % domain
            return HttpResponseRedirect(url)


def set_team(backend, details, response, is_new, user=None, *args, **kwargs):
    if backend.name == "slack" and not "team_id" in kwargs["social"].extra_data:
        team_id = response["team"]["id"]
        social = kwargs["social"]
        social.set_extra_data({"team_id": team_id})
        social.save()


def not_allowed(request):
    if request.user.is_authenticated():
        # otherwise they land on this page after they fail once and then log in for real
        return HttpResponseRedirect("/")
    return TemplateResponse(request, "slack-domain-not-allowed.html", {})


def slack_redirect(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    team = user.social_auth.filter(provider="slack")[0].extra_data["team"]
    return HttpResponseRedirect("%smessages/@%s" % (team["url"], username))


def get_additional_permissions(request):
    slack_name = "we-evolve"
    path = "/complete/slack/"
    params = {
        "client_id": settings.SOCIAL_AUTH_SLACK_KEY,
        "redirect_uri": f"{settings.SITE_ORIGIN}{path}",
        "scope": ",".join(settings.EXTRA_SLACK_SCOPE),
        "state": "",  # random string to track back?
    }
    f"https://{slack_name}.slack.com/oauth?{qs}"
