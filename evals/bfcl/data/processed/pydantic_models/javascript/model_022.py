# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:38+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class ResetStateProperty(BaseModel):
    stateProperty: str = Field(
        ..., description='The name of the state property to reset.'
    )
