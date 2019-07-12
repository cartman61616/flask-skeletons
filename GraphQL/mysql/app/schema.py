import graphene
from graphene import ObjectType, String


class ExampleQuery(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "Hello"


class RootQuery(ExampleQuery, ObjectType):
    pass


schema = graphene.Schema(query=RootQuery)
