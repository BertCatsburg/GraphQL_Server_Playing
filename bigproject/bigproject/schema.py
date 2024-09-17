import graphene


class MyQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class MyMutation(graphene.Mutation):
    pass


schema = graphene.Schema(
    query=MyQuery,
    mutation=MyMutation
)