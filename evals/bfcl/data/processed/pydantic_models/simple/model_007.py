# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:37+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CalculateCircumference(BaseModel):
    radius: int = Field(..., description='The radius of the circle in the unit given.')
    unit: Optional[str] = Field(
        None, description="The unit of measurement for the radius. Default is 'cm'."
    )
