# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:44+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SortBy(Enum):
    popularity = 'popularity'
    chronological = 'chronological'
    alphabetical = 'alphabetical'


class MetropolitanMuseumGetTopArtworks(BaseModel):
    number: int = Field(..., description='The number of artworks to fetch')
    sort_by: Optional[SortBy] = Field(
        SortBy.popularity,
        description="The criteria to sort the results on. Default is 'popularity'.",
    )