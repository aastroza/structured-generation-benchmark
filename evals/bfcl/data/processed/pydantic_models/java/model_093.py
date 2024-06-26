# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:18+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class AbstractjaragentRunjaragent(BaseModel):
    options: str = Field(
        ..., description='The options for the jar agent, separated by spaces.'
    )
    inst: str = Field(
        ...,
        description='The Instrumentation instance to which the agent will be attached.',
    )
