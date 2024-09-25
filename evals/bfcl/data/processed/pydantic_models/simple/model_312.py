# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class PlayerStatistic(BaseModel):
    player_name: str = Field(..., description="The player's name.")
    year: int = Field(
        ..., description='Year for which the statistics will be displayed.'
    )
    team_name: Optional[str] = Field(
        '',
        description='The name of the team(optional). Default to not use it if not specified.',
    )