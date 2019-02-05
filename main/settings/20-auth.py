SOCIAL_AUTH_SLACK_SCOPE = []  # "team:read", "channels:history", "channels:read"]
SOCIAL_AUTH_POSTGRES_JSONFIELD = True


AUTHENTICATION_BACKENDS = (
    "social.backends.slack.SlackOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)
