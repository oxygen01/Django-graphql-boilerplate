import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ...models import Link

#1
class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ['url', 'description']


#2
class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        #3
        interfaces = (graphene.relay.Node, )


class RelayQuery(graphene.ObjectType):
    #4
    relay_link = graphene.relay.Node.Field(LinkNode)
    #5
    relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)