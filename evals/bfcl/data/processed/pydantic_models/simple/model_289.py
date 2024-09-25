# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:54+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class ConcertFindNearby(BaseModel):
    location: str = Field(..., description='The city and state, e.g. Seattle, WA')
    genre: str = Field(..., description='Genre of music to be played at the concert.')