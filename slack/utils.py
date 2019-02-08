from django.conf import settings

from .models import SlackChannel, SlackUser, SlackMessage

from slackclient import SlackClient
import json
import time


def pprint(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def get_client():
    return SlackClient(settings.SLACK_TOKEN)


# def create_channels():
#     sc = get_client()
#     channels_list = sc.api_call("channels.list")
#     for channel in channels_list["channels"]:
#         SlackChannel.ninja_add(channel)


def log_channels():
    i = 0
    sc = get_client()
    users_list = sc.api_call("users.list")
    for user in users_list["members"]:
        SlackUser.ninja_add(user)
    channels_list = sc.api_call("channels.list")
    bot_id = sc.api_call("auth.test")["user_id"]
    for data in channels_list["channels"]:
        channel = SlackChannel.ninja_add(data)
        if not channel.watching:
            continue

        """if not data['is_member']:
            print(sc.api_call('channels.join',channel=channel.id))"""

        message_count = channel.slackmessage_set.count()
        channel.save()
        history = sc.api_call("conversations.history", channel=channel.id)
        for m in history["messages"]:
            if not "user" in m:
                if not "bot_id" in m:
                    print("BAD MESSAGE:\n%s\n\n" % m)
                continue
            SlackMessage.ninja_add(m, channel=channel)
        i += 1
        print(channel, message_count, channel.slackmessage_set.count())


def listen():
    sc = get_client()
    if sc.rtm_connect(with_team_state=False):
        print("Connected!")
        starterbot_id = sc.api_call("auth.test")["user_id"]
        while True:
            print(sc.rtm_read())
            time.sleep(1)
    else:
        print("Connection failed. Exception traceback printed above.")
