# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class FungamebaseOnfinish(BaseModel):
    layout: str = Field(
        ...,
        description='The RefreshLayout instance associated with the FunGame refresh header.',
    )
    success: bool = Field(
        ..., description='Indicates whether the refresh operation was successful.'
    )
