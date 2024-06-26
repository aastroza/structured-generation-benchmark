# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:55+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class VOe(BaseModel):
    r: str = Field(..., description='The object to update.')
    e: str = Field(..., description='The property of the object to update.')
    t: str = Field(..., description='The new value to assign to the property.')
