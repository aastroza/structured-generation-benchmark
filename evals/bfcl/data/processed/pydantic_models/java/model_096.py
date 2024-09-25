# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:20+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class InstrumentableprocessorCreatecallconverter(BaseModel):
    converterMethod: str = Field(
        ..., description='The ExecutableElement representing the converter method.'
    )
    frameParameterName: str = Field(
        ..., description='The name of the frame parameter to be used in the call.'
    )
    returnName: str = Field(
        ..., description='The CodeTree representing the name of the return value.'
    )