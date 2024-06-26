# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:53+00:00

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel, Field


class XcontentbuilderMap(BaseModel):
    values: Dict[str, Any] = Field(
        ..., description='The map of values to serialize into the XContentBuilder.'
    )
    ensureNoSelfReferences: bool = Field(
        ...,
        description='A flag to ensure the map does not contain references to itself, which could cause a stackoverflow error.',
    )
    writeStartAndEndHeaders: bool = Field(
        ...,
        description='A flag to indicate whether to write the start and end object headers.',
    )
