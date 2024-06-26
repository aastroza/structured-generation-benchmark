# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:34+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetCollectablesInSeason(BaseModel):
    game_name: str = Field(..., description='Name of the game.')
    season: str = Field(
        ..., description='The season for which to retrieve the collectable items.'
    )
    item_type: Optional[str] = Field(
        'all',
        description="The type of item to search for. Default is 'all'. Possible values: 'all', 'bug', 'fish', 'sea creatures', etc.",
    )
