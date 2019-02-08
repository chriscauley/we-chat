from django.template.response import TemplateResponse
from django.http import JsonResponse

from .models import SlackMessage, SlackChannel, SlackUser

import random


def random_message(request):
    return TemplateResponse(
        request, "rando.xml", {"message": SlackMessage.objects.all().order_by("?")[0]}
    )


def channel_messages(request, channel_id):
    channel = SlackChannel.objects.get(id=channel_id)
    messages = SlackMessage.objects.filter(channel__id=channel_id)
    return JsonResponse(
        {"messages": [m.data for m in messages], "channel": channel.data}
    )


def channel_list(request):
    channels = SlackChannel.objects.all()
    return JsonResponse({"results": [c.data for c in channels]})


def member_query(request):
    ids = json.loads(request.GET["ids"])
    users = SlackUser.objects.filter(id__in=ids)
    return JsonResponse({"users": [u.data for u in users]})
