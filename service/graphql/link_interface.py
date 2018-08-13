import graphene

class LinkInterface(graphene.Interface):
    relationship = graphene.String()
    target = graphene.String()
