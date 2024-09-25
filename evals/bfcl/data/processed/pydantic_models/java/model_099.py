# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class LibraryexportCreatedelegate(BaseModel):
    factory: str = Field(
        ...,
        description='The factory used to create a new delegate instance of the library.',
    )
    delegate: str = Field(
        ..., description='The existing delegate instance of the library.'
    )