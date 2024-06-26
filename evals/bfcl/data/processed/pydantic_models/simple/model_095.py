# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:54:38+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class CalcAreaTriangle(BaseModel):
    base: int = Field(
        ..., description='The length of the base of the triangle in meters.'
    )
    height: int = Field(
        ...,
        description='The perpendicular height of the triangle from the base to the opposite vertex in meters.',
    )
