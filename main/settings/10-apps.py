INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "social.apps.django_app.default",
    "social_django",
    "graphene_django",
    # project apps
    "main",
    "slack",
]


GRAPHENE = {"SCHEMA": "main.schema.schema"}
