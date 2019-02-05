from django.contrib import admin
from django.urls import path, include, re_path

import unrest.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path('', include(unrest.urls)),
]
