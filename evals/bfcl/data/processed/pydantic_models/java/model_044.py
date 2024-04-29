# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:43+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class DesapitestInit(BaseModel):
    crypt: str = Field(
        ..., description="The encryption algorithm to use, such as 'DES' or 'DESede'."
    )
    mode: str = Field(
        ..., description="The cipher mode to use, such as 'CBC' or 'ECB'."
    )
    padding: str = Field(
        ...,
        description="The padding scheme to use, such as 'PKCS5Padding' or 'NoPadding'.",
    )
