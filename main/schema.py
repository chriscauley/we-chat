from django.contrib.auth import get_user_model
from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
import datetime


class UserType(DjangoObjectType):
    # has_password = graphene.Boolean()

    # def resolve_has_password(instance, info):
    #    return bool(instance.password)
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    today = graphene.String()
    user = graphene.Field(UserType)

    def resolve_user(self, info):
        print(1, info.context.user)
        if info.context.user.is_authenticated:
            return info.context.user


schema = graphene.Schema(query=Query)
