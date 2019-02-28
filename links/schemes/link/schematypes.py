from graphene_django import DjangoObjectType
from ...models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link
