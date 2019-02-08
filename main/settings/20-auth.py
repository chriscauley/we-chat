EXTRA_SLACK_SCOPE = ["team:read", "channels:history", "channels:read", "users:read"]
SOCIAL_AUTH_POSTGRES_JSONFIELD = True


AUTHENTICATION_BACKENDS = (
    "social_core.backends.slack.SlackOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "slack.auth.views.validate_team",
    "slack.auth.views.associate_by_slack_name",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "social_core.pipeline.social_auth.associate_by_email",
    "slack.auth.views.set_team",
)

ALLOWED_SLACK_TEAMS = ["TFSGCTN4F"]

LOGIN_REDIRECT_URL = "/"
