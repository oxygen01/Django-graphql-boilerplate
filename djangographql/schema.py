import graphene
import graphql_jwt

import links.schemes.link.query
import links.schemes.link.mutation
import users.schemes.user.mutation
import users.schemes.user.query


class Query(links.schemes.link.query.Query,
            users.schemes.user.query.Query,
            graphene.ObjectType):
    pass


class Mutation(links.schemes.link.mutation.Mutation,
               users.schemes.user.mutation.Mutation,
               graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field() # use it to login
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
