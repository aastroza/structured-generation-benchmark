# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:27+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class MapTransitions(BaseModel):
    category: str = Field(
        ..., description='The category to be assigned to each element in the mapping.'
    )
    limit: float = Field(
        ...,
        description='The number of elements from the array to include in the mapping. This is a float type value.',
    )
