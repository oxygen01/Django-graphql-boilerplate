import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from ...models import Link
from users.schemes.user.schematypes import UserType


class DeleteLink(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int();

    def mutate(self, info, id):
        try:
            Link.objects.get(id=id).delete()
            return DeleteLink(message=f"{id} is deleted")
        except Exception as e:
            raise GraphQLError(str(e))


class CreateLink(graphene.Mutation):
    # return
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, url, description):
        user = info.context.user
        if user.is_anonymous:
            raise Exception(f'Not authorized!. {user}')
        try:
            link = Link(url=url, description=description, posted_by=user)
            link.save()
            # return link
            # Or for custom return
            return CreateLink(id=link.id,
                              url=link.url,
                              description=link.description,
                              posted_by=link.posted_by)
        except Exception as e:
            raise GraphQLError(str(e))


# 4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    delete_link = DeleteLink.Field()
