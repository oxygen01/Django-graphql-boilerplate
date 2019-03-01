import graphene
import django_filters
from graphene_django.filter import DjangoFilterConnectionField

from ...models import Link
from .schemanodes import LinkNode
#1
class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ['url', 'description']

class Query(graphene.ObjectType):
    #4
    relay_link = graphene.relay.Node.Field(LinkNode)
    #5
    relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)