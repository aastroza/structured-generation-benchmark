# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:53:46+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class MathHcf(BaseModel):
    number1: int = Field(..., description='First number.')
    number2: int = Field(..., description='Second number.')
