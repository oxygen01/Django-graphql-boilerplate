import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from ...models import Link
from .schematypes import LinkType


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)
    link = graphene.Field(LinkType, id=graphene.Int())

    def resolve_links(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception(f'Not authorized!. {user}')
        return Link.objects.all()

    def resolve_link(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not authorized!')
        id = kwargs.get('id')
        try:
            return Link.objects.get(id=id)
        except:
            raise GraphQLError('Not found')
