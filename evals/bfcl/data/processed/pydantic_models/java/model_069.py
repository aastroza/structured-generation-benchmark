# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:01+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class DurationimplAlignsigns(BaseModel):
    buf: List[str] = Field(
        ...,
        description='The array of BigDecimal elements representing different units of time whose signs need to be aligned.',
    )
    start: int = Field(
        ..., description='The starting index of the subarray to align signs.'
    )
    end: int = Field(
        ..., description='The ending index of the subarray to align signs.'
    )