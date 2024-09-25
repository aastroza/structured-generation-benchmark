# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:23+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class PopulationProjections(BaseModel):
    country: str = Field(
        ..., description='The country for which to calculate the population projection.'
    )
    years: int = Field(..., description='Number of years for the projection.')
    growth_rate: Optional[float] = Field(
        1.2,
        description='Optional parameter to specify the growth rate, in percentage. Default is 1.2. This is a float type value.',
    )