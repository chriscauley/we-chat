from django.contrib import admin
from django.urls import path, include, re_path

import unrest.urls

urlpatterns = [
    path("", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
    path("", include(unrest.urls)),
]
