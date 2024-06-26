# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:39+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class SculptureLocatorFindByArtist(BaseModel):
    artist: str = Field(..., description='Name of the Artist of the sculpture')
    material: str = Field(..., description='Material of the sculpture.')
    location: Optional[str] = Field(
        'all',
        description="The location where you want to find the sculpture. Default is 'all' if not specified.",
    )
