import graphene
from graphene import String, relay, Field
from graphql import GraphQLError
from ...models import Link
from .schemanodes import LinkNode
from graphql_relay.node.node import from_global_id

class RelayDeleteLink(relay.ClientIDMutation):
    message = String()

    class Input:
        link_id = String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception(f'Not authorized!.')
        try:
            id = from_global_id(input.get('link_id'))[1] # to decode the relay ID(id in base64 encoded)
            link = Link.objects.get(id=id) #.delete()
            return RelayDeleteLink(message=f"{link.url} is deleted")
        except Exception as e:
            raise GraphQLError(str(e))


class RelayCreateLink(relay.ClientIDMutation):
    link = Field(LinkNode)

    class Input:
        url = String()
        description = String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None
        if user.is_anonymous:
            raise Exception(f'Not authorized!.')
        try:
            link = Link(
                url=input.get('url'),
                description=input.get('description'),
                posted_by=user,
            )
            link.save()

            return RelayCreateLink(link=link)
        except Exception as e:
            raise GraphQLError(str(e))


class Mutation(graphene.AbstractType):
    relay_create_link = RelayCreateLink.Field()
    relay_delete_link = RelayDeleteLink.Field()
