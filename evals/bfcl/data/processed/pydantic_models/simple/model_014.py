# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateDerivative(BaseModel):
    function: str = Field(..., description='The polynomial function.')
    x_value: Optional[float] = Field(
        0.0,
        description='The x-value at which the derivative is calculated. Optional, default to 0.00. This is a float type value.',
    )