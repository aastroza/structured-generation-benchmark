# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:41+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class CalculateAreaUnderCurve(BaseModel):
    function: str = Field(..., description='The mathematical function as a string.')
    interval: List[float] = Field(
        ...,
        description='An array that defines the interval to calculate the area under the curve from the start to the end point.',
    )
    method: Optional[str] = Field(
        None,
        description="The numerical method to approximate the area under the curve. The default value is 'trapezoidal'.",
    )
