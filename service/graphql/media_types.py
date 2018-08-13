import graphene

from .link_interface import LinkInterface

class MediaInterface(graphene.Interface):

    participant = graphene.List(lambda: ParticipantResult, relationship= graphene.ID())

    def resolve_participant(self, info, relationship = None ):
        return [
            resolve_target(f.target.lower())
            for f in self.links
            if f.target.lower().startswith("entity/") and (
                relationship is None or f.relationship == relationship
            )
        ]

class MovieMediaDetail(graphene.ObjectType):
    class Meta:
        interfaces = (LinkInterface, MediaInterface)

    id = graphene.String()
    title = graphene.String()
    premier = graphene.String()
    sequel = graphene.String()

class ShowMediaDetails(graphene.ObjectType):
    class Meta:
        interfaces = (LinkInterface, MediaInterface)

    id = graphene.String()
    title = graphene.String()
    premier = graphene.String()
    seasons = graphene.String()
    episodes = graphene.String()

class MediaResult(graphene.Union):

    class Meta:
        types = (MovieMediaDetail, ShowMediaDetails)

    def resolve_type(self, info):
        if "movie" in self.id:
            return MovieMediaDetail

        if "show" in self.id:
            return ShowMediaDetails

from .graphql_data import resolve_target
from .participant_types import ParticipantResult
