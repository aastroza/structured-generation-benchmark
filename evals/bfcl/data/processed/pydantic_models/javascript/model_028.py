# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:59:43+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class FilterBooksByAuthor(BaseModel):
    library: List[str] = Field(
        ..., description='The collection of book objects to filter through.'
    )
    author: str = Field(
        ..., description='The name of the author whose books you want to find.'
    )