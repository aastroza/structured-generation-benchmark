# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:08+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SaxfilterfactoryimplResolveentity(BaseModel):
    publicid: str = Field(
        ..., description='The public identifier of the entity to resolve.'
    )
    sysId: str = Field(
        ..., description='The system identifier of the entity to resolve.'
    )
