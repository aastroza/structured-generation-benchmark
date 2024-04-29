# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:28+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MapRoutingFastestRoute(BaseModel):
    start_location: str = Field(
        ..., description='The starting location for the journey.'
    )
    end_location: str = Field(..., description='The destination for the journey.')
    avoid_tolls: Optional[bool] = Field(
        None,
        description='Option to avoid toll roads during the journey. Default is false.',
    )
