import graphene

from .graphql_data import resolve_target
from .media_types import MediaResult
from .participant_types import ParticipantResult


class Query(graphene.ObjectType):

    media = graphene.Field(MediaResult, id = graphene.ID())
    participant = graphene.Field(ParticipantResult, id = graphene.ID())

    def resolve_media(self, info, id):
            return resolve_target(id)

    def resolve_participant(self, info, id):
        return resolve_target(id)

schema = graphene.Schema(query=Query)