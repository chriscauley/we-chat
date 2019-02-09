from django.urls import path
import slack.views

urlpatterns = [
    path("api/channel/<channel_id>/messages/", slack.views.channel_messages),
    path("api/channel/", slack.views.channel_list),
    path("api/user/", slack.views.user_query),
]
