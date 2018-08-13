import graphene

from .link_interface import LinkInterface

class ParticipantInterface(graphene.Interface):

    media = graphene.List(lambda: MediaResult, relationship= graphene.ID())

    def resolve_media(self, info, relationship = None ):
        return [
            resolve_target(f.target.lower())
            for f in self.links
            if f.target.lower().startswith("media/") and (
                relationship is None or f.relationship == relationship
            )
        ]


class CompanyDetails(graphene.ObjectType):
    class Meta:
        interfaces = (LinkInterface, ParticipantInterface)

    id = graphene.ID()
    companyName = graphene.String()
    founded = graphene.String()
    type = graphene.String()

class PersonDetails(graphene.ObjectType):
    class Meta:
        interfaces = (LinkInterface, ParticipantInterface)

    id = graphene.ID()
    name = graphene.String()
    yearsActive = graphene.String()
    dob = graphene.String()
    type = graphene.String()


class ParticipantResult(graphene.Union):

    class Meta:
        types = (CompanyDetails, PersonDetails)

    def resolve_type(self, info):
        if "company" in self.type:
            return CompanyDetails
        elif "person" in self.type:
            return PersonDetails
        else: raise BaseException

from .media_types import MediaResult
from .graphql_data import resolve_target

