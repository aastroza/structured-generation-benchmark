# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:23+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class Res9PatchstreamdecoderDecode(BaseModel):
    input: str = Field(
        ..., description='The input stream containing the 9-patch image data.'
    )
    out: str = Field(
        ...,
        description='The output stream where the decoded PNG image will be written.',
    )
