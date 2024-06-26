# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:07+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class OptionspecbuilderRequiredunless(BaseModel):
    dependent: str = Field(..., description='The primary dependent option name.')
    otherDependents: Optional[List[str]] = Field(
        None,
        description='Other dependent option names that can make the current option non-required. Default empty array',
    )
