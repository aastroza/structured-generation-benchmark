# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:54+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ProbabilityOfEvent(BaseModel):
    success_outcomes: int = Field(..., description='The number of successful outcomes.')
    total_outcomes: int = Field(
        ..., description='The total number of possible outcomes.'
    )
    format_as_ratio: Optional[bool] = Field(
        False,
        description='When true, formats the output as a ratio instead of a decimal. Default is false.',
    )