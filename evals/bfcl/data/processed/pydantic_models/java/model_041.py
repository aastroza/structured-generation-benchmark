# generated by datamodel-codegen:
#   filename:  json_schema.json
#   timestamp: 2024-04-29T20:58:41+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SearchhitDeclareinnerhitsparsefields(BaseModel):
    parser: str = Field(..., description='The ObjectParser instance to configure.')
