# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:52+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Queue1(BaseModel):
    worker: str = Field(
        ..., description='The worker function that processes each task.'
    )
    concurrency: float = Field(
        ...,
        description='The maximum number of tasks to be processed concurrently. This is a float type value.',
    )
    payload: Optional[float] = Field(
        0.0,
        description='Optional. The number of tasks each worker function call should process at most. Default 0.0 This is a float type value.',
    )
