# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:09+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetCareerStats(BaseModel):
    player_name: str = Field(..., description='The name of the basketball player.')
    team: Optional[str] = Field(
        '',
        description='The team that the player currently plays for or has played for (Optional). Default to use all teams if not specified.',
    )
