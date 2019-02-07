from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models

import re


class SlackModel(models.Model):
    class Meta:
        abstract = True

    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=128)
    data = JSONField(default=dict)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def ninja_add(clss, json, **defaults):
        defaults = {"name": json["name"], **defaults}
        obj, new = clss.objects.get_or_create(id=json["id"], defaults=defaults)
        if new:
            print("created: %s" % obj.name)
        for key, value in defaults.items():
            setattr(obj, key, value)
        obj.data = json
        obj.save()
        return obj


class SlackChannel(SlackModel):
    watching = models.BooleanField(default=False)


class SlackUser(SlackModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )


class SlackMessage(models.Model):
    data = JSONField(default=dict)
    updated = models.DateTimeField(auto_now=True)

    channel = models.ForeignKey(SlackChannel, on_delete=models.CASCADE)
    slackuser = models.ForeignKey(SlackUser, on_delete=models.CASCADE)
    ts = models.CharField(
        max_length=20
    )  # timestamp, used with slackuser and channel to ensure uniqueness

    @classmethod
    def ninja_add(clss, json, **defaults):
        slackuser = SlackUser.objects.get_or_create(id=json["user"])[0]
        ts = json["ts"]
        if not "channel" in defaults:
            raise NotImplementedError

        obj, new = clss.objects.get_or_create(
            ts=ts, slackuser=slackuser, defaults=defaults
        )
        if new:
            print("created: message #", obj.id)
        for key, value in defaults.items():
            setattr(obj, key, value)
        obj.data = json
        obj.save()
        return obj
