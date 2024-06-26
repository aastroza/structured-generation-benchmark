# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:51+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ProbDistBinomial(BaseModel):
    trials: int = Field(..., description='The number of independent experiments.')
    successes: int = Field(..., description='The number of success events.')
    p: Optional[float] = Field(
        0.5,
        description='The probability of success on any given trial, defaults to 0.5 This is a float type value.',
    )
