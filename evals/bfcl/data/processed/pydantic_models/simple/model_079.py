# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:27+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class CreateHistogram(BaseModel):
    data: List[int] = Field(
        ..., description='The data for which histogram needs to be plotted.'
    )
    bins: int = Field(
        ..., description='The number of equal-width bins in the range. Default is 10.'
    )
