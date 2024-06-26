# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class HistoricalContribGetContrib(BaseModel):
    scientist: str = Field(
        ..., description='The scientist whose contributions need to be searched.'
    )
    date: str = Field(
        ..., description='The date when the contribution was made in yyyy-mm-dd format.'
    )
    category: Optional[str] = Field(
        'all',
        description="The field of the contribution, such as 'Physics' or 'Chemistry'. Default is 'all'.",
    )
