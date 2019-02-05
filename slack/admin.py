from django.contrib import admin

from .models import SlackChannel, SlackUser, SlackMessage


class SlackAdmin(admin.ModelAdmin):
    readonly_fields = ["data"]


@admin.register(SlackChannel)
class SlackChannelAdmin(SlackAdmin):
    list_display = ["name", "watching"]


@admin.register(SlackUser)
class SlackUserAdmin(SlackAdmin):
    pass


@admin.register(SlackMessage)
class SlackMessageAdmin(SlackAdmin):
    pass
