import graphene
from graphql import GraphQLError
from ...models import Link
from .schemanodes import LinkNode

class RelayCreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

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
