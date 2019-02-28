import graphene
from graphql_jwt.shortcuts import get_token
import graphql_jwt
from graphql import GraphQLError

from django.contrib.auth import get_user_model
from .schematypes import UserType

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String();

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        try:
            user = get_user_model()(username=username, email=email)
            user.set_password(password)
            user.save()
            return CreateUser(user=user,
                              token = get_token(user)
                              )
        except Exception as e:
            raise GraphQLError(str(e))

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
