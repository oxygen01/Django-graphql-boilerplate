import graphene
from graphene_django import DjangoObjectType
from ...models import Link

class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        #3
        interfaces = (graphene.relay.Node, )
