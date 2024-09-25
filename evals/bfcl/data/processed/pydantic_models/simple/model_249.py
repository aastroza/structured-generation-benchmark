# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:56:26+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ReligionHistoryInfo(BaseModel):
    religion: str = Field(
        ...,
        description='The name of the religion for which historical details are needed.',
    )
    till_century: int = Field(
        ..., description='The century till which historical details are needed.'
    )
    include_people: Optional[bool] = Field(
        False,
        description='To include influential people related to the religion during that time period, default is False',
    )