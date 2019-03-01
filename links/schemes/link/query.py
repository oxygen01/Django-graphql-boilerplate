import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from ...models import Link
from .schematypes import LinkType
from django.db.models import Q

class Query(graphene.ObjectType):
    links = graphene.List(LinkType,
                            search =graphene.String(),
                            first = graphene.Int(),
                            skip = graphene.Int())
    link = graphene.Field(LinkType, id=graphene.Int())

    def resolve_links(self, info,search = None, first=None, skip=None, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception(f'Not authorized!. {user}')
        
        linksList = Link.objects.all()

        #search = kwargs.get('search')
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )
            return linksList.filter(filter)    

        if skip:
            linksList = linksList[skip:]

        if first:
            linksList = linksList[:first]    
        
        return linksList

    def resolve_link(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not authorized!')
        id = kwargs.get('id')
        try:
            return Link.objects.get(id=id)
        except:
            raise GraphQLError('Not found')
