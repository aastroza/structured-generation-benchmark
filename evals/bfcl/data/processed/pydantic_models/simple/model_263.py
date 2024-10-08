# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:36+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetSculptureInfo(BaseModel):
    artist_name: str = Field(..., description='The name of the artist.')
    year: Optional[int] = Field(
        '',
        description='Year of the sculpture. This is optional. Default is the most recent year.',
    )
    detail: Optional[bool] = Field(
        False,
        description='If True, it provides detailed description of the sculpture. Defaults to False.',
    )
