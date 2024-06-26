# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:57:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ScaleType(Enum):
    major = 'major'
    minor = 'minor'


class MusicTheoryKeySignature(BaseModel):
    key: str = Field(..., description="The root of the scale, e.g., 'C', 'F#', 'Ab'.")
    scale_type: Optional[ScaleType] = Field(
        ScaleType.major,
        description="Type of the scale, either 'major' or 'minor'. Default is 'major'.",
    )
