from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView

import unrest.urls

urlpatterns = [
    path("", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
    path("", include(unrest.urls)),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]
