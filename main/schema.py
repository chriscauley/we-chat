from django.contrib.auth import get_user_model
from django.conf import settings
from graphene_django import DjangoObjectType

import graphene
import datetime


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    def resolve_user(self, info):
        if info.context.user.is_authenticated:
            return info.context.user


schema = graphene.Schema(query=Query)
