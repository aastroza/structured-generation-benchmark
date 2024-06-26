# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:04+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class EncodingsGetencodinginfo(BaseModel):
    encoding: str = Field(..., description='The IANA or Java encoding name.')
    allowJavaNames: bool = Field(
        ..., description='Flag to determine if Java encoding names are allowed.'
    )
