# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:56+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GetCurrentTime(BaseModel):
    city: str = Field(
        ..., description='The city for which the current time is to be retrieved.'
    )
    country: str = Field(..., description='The country where the city is located.')
    format: Optional[str] = Field(
        'HH:MM:SS',
        description="The format in which the time is to be displayed, optional (defaults to 'HH:MM:SS').",
    )